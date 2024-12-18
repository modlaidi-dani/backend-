from rest_framework import serializers
from .models import *
from clientInfo.serializers import *
from user.serializers import *
from produits.serializers import * 
from ventes.serializers import *
from tiers.serializers import *
from comptoire.serializers import *

class EntrepotSerializer(serializers.ModelSerializer):
    responsables=serializers.SerializerMethodField()
    stocks=serializers.SerializerMethodField()
    store=StoreSerializer()
    class Meta:
        model=Entrepot
        fields="__all__"
    def get_responsables(self,obj):
       users = obj.responsables.all()
       list_responsables = []
       for user in users :
           list_responsables.append(user.username)
       return list_responsables
    def get_stocks(self,obj):
       return obj.inventories.all()

class equipeInventaireSerializer(serializers.ModelSerializer):
    class Meta:
        model=equipeInventaire
        fields="__all__"
class produitEnInventaireAnnuelSerializer(serializers.ModelSerializer):
    Equipe=equipeInventaireSerializer()
    product=ProductSerializer()
    class Meta:
        model=produitEnInventaireAnnuel
        fields="__all__"
class InventaireAnnuelSerializer(serializers.ModelSerializer):
    equipe=equipeInventaireSerializer(source="inventaire_assosiated")
    entrepot=EntrepotSerializer()
    store=StoreSerializer()
    class Meta:
        model=InventaireAnnuel
        fields="__all__"
class ProduitsEnBonRetourAncienSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitsEnBonRetourAncien
        fields="__all__"
class BonRetourAncienSerializer(serializers.ModelSerializer):
    produits=ProduitsEnBonRetourAncienSerializer(source="produits_en_bon_retourancien",many=True)
    user=CustomUserSerializer()
    entrepot=EntrepotSerializer()
    store=StoreSerializer()
    total_price_retour=serializers.SerializerMethodField()
    class Meta:
        model=BonRetourAncien
        fields="__all__"
    def get_total_price_retour(self,obj):
        return round(sum(Decimal(product.unitprice) * product.quantity for product in obj.produits_en_bon_retourancien.all()),2)


class StockSerializer(serializers.ModelSerializer):
    product=ProductSerializer()
    entrepot=EntrepotSerializer()
    quantity_detailed=serializers.SerializerMethodField()
    quantity=serializers.SerializerMethodField()
    historical_entered_quantity=serializers.SerializerMethodField()
    historical_received_quantity=serializers.SerializerMethodField()
    historical_transfered_quantity=serializers.SerializerMethodField()
    product_sold_quantity=serializers.SerializerMethodField()
    product_returned_quantity=serializers.SerializerMethodField()
    quantity_expected=serializers.SerializerMethodField()
    class Meta:
        model=Stock
        fields="__all__"
    
    def get_quantity_detailed(self,obj):
        return obj.quantity - obj.quantity_blocked
        
    
    def get_quantity(self,obj):
        return obj.quantity - obj.quantity_blocked
    
    def get_historical_entered_quantity(self,obj):
        # Calculate quantity from entry transactions
        entry_quantity = ProduitsEnBonEntry.objects.filter(stock=obj.product, BonNo__entrepot=obj.entrepot).aggregate(models.Sum('quantity'))['quantity__sum'] or 0
        return obj.quantity_initial + entry_quantity
        
    
    def get_historical_received_quantity(self,obj):
        # Calculate quantity from transfer transactions where this stock is the destination
        transfer_arrived_quantity = ProduitsEnBonTransfert.objects.filter(
                stock_arr=obj, 
                BonNo__entrepot_arrive=obj.entrepot,
                BonNo__automatiquement=F('BonNo__valide')  # Both true or both false
        ).aggregate(models.Sum('quantity'))['quantity__sum'] or 0
        transfer_mag_quantity = ProduitsEnBonTransfertMag.objects.filter(stock_arr=obj, BonNo__entrepot_arrive=obj.entrepot).aggregate(models.Sum('quantity'))['quantity__sum'] or 0
        return transfer_arrived_quantity + transfer_mag_quantity
        
    
    def get_historical_transfered_quantity(self,obj):
        # Calculate quantity from transfer transactions where this stock is the source
        transfer_departed_quantity = ProduitsEnBonTransfert.objects.filter(
                stock_dep=obj, 
                BonNo__entrepot_depart=obj.entrepot,
                BonNo__automatiquement=F('BonNo__valide')  # Both true or both false
        ).aggregate(models.Sum('quantity'))['quantity__sum'] or 0
        transfert_mag = ProduitsEnBonTransfertMag.objects.filter(stock_dep=obj, BonNo__entrepot_depart=obj.entrepot).aggregate(models.Sum('quantity'))['quantity__sum'] or 0
        return transfer_departed_quantity + transfert_mag
    
    
    def get_product_sold_quantity(self,obj):
        produits_en_bon_comptoir = ProduitsEnBonComptoir.objects.filter(
                    stock=obj.product,
                )
           # Filter the instances based on the condition specified in monentrepot
        filtered_produits = [produit for produit in produits_en_bon_comptoir if produit.BonNo.monentrepot == obj.entrepot.name]
        
                # Sum up the quantities from the filtered instances
        comptoir_quantity = sum(produit.quantity for produit in filtered_produits)
        produits_en_bon_sortie_list = ProduitsEnBonSortie.objects.filter(
            stock=obj.product,
            BonNo__entrepot=obj.entrepot
        )

        filtered_produits_en_bon_sortie = [
            produit_en_bon_sortie for produit_en_bon_sortie in produits_en_bon_sortie_list
            if produit_en_bon_sortie.BonNo.get_etat_transfert == True
        ]
        
        # Calculate the sum of quantities for the filtered objects
        sold_quantity = sum(produit_en_bon_sortie.quantity for produit_en_bon_sortie in filtered_produits_en_bon_sortie)
        return sold_quantity + comptoir_quantity
        
    
    def get_product_returned_quantity(self,obj):
        produits_en_bon_comptoir = ProduitsEnBonRetourComptoir.objects.filter(
                    produit=obj.product,
                )
           # Filter the instances based on the condition specified in monentrepot
        filtered_produits = [produit for produit in produits_en_bon_comptoir if produit.BonNo.bon_comptoir_associe.monentrepot == obj.entrepot.name ]
        produits_en_bon_retour= ProduitsEnBonRetour.objects.filter(
                    produit=obj.product,
                )
        filtered_retour_produits = [produit for produit in produits_en_bon_retour if produit.BonNo.bonL.entrepot == obj.entrepot and produit.reintegrated and produit.BonNo.valide]
        comptoir_returned_quantity = sum(produit.quantity for produit in filtered_produits)   
        returned_quantity = sum(produit.quantity for produit in filtered_retour_produits)   

        return comptoir_returned_quantity + returned_quantity

    
    def get_quantity_expected(self,obj):
        total_entered_quantity = obj.historical_entered_quantity + obj.historical_received_quantity + obj.product_returned_quantity
        total_out_quantity = obj.product_sold_quantity + obj.historical_transfered_quantity
        return total_entered_quantity - total_out_quantity  
class ProduitsEnBonTransfertMagSerializer(serializers.ModelSerializer):
    stock_dep=StockSerializer()
    stock_arr=StockSerializer()
    class Meta:
        model=ProduitsEnBonTransfertMag
        fields="__all__"
class BonTransfertMagasinSerializer(serializers.ModelSerializer):
    produits=ProduitsEnBonTransfertMag()
    store_depart=StoreSerializer()
    entrepot_depart=EntrepotSerializer()
    store_arrive=StoreSerializer()
    entrepot_arrive =EntrepotSerializer()
    user=CustomUserSerializer()
    store=StoreSerializer()
    class Meta:
        model=BonTransfertMagasin
        fields="__all__"
class ProduitsEnBonRetourSerializer(serializers.ModelSerializer):
    produit=ProductSerializer()
    class Meta:
        model=ProduitsEnBonRetour
        fields="__all__"
class BonRetourSerializer(serializers.ModelSerializer):
    produits=ProduitsEnBonRetourSerializer(source="produits_en_bon_retour",many=True)
    bonL=BonSortieSerializer()
    client=ClientSerializer()
    user=CustomUserSerializer()
    store=StoreSerializer()
    reintegrated=serializers.SerializerMethodField()
    total_price_retour=serializers.SerializerMethodField()
    class Meta:
        model=BonRetour
        fields="__all__"
    def get_reintegrated(self,obj):
        return obj.produits_en_bon_retour.first().reintegrated

    def get_total_price_retour(self,obj):
        return round(sum(Decimal(product.unitprice) * product.quantity for product in obj.produits_en_bon_retour.all()),2)
class ProduitsEnBonEchangeSerializer(serializers.ModelSerializer):
    stock=ProductSerializer()
    class Meta:
        model=ProduitsEnBonEchange
        fields="__all__"
class BonEchangeSerializer(serializers.ModelSerializer):
    produits=ProduitsEnBonEchangeSerializer(source="ProduitsEnBonEchange",many=True)
    bonL=BonRetourSerializer()
    client=ClientSerializer()
    entrepot=EntrepotSerializer()
    user=CustomUserSerializer()
    store=StoreSerializer()
    class Meta:
        model=BonEchange
        fields="__all__"
class ProduitsEnBonMaintenanceSerializer(serializers.ModelSerializer):
    produit=ProductSerializer()
    Observation=serializers.SerializerMethodField()
    image1=serializers.SerializerMethodField()
    image2=serializers.SerializerMethodField()
    image3=serializers.SerializerMethodField()
    image4=serializers.SerializerMethodField()
    
    class Meta:
        model=ProduitsEnBonMaintenance
        fields="__all__"

    def get_Observation(self,obj):
        return eval(obj.observation) if '\'' in obj.observation else list(obj.observation)
        
    def get_image1(self,obj):
        if obj.image1:
                return obj.image1.url
        else:
                return ''
    def get_image2(self,obj):
        if obj.image1:
                return obj.image1.url
        else:
                return ''
    def get_image3(self,obj):
        if obj.image1:
                return obj.image1.url
        else:
                return ''
    def get_image4(self,obj):
        if obj.image1:
                return obj.image1.url
        else:
                return ''
class BonMaintenanceSerializer(serializers.ModelSerializer):
    produits=ProduitsEnBonMaintenanceSerializer(source="produits_en_bon_maintenance",many=True)
    bonL=BonRetourSerializer()
    bonR=BonRetourAncienSerializer()
    bonLComptoir=BonRetourComptoirSerializer()
    entrepot=EntrepotSerializer()
    user=CustomUserSerializer()
    store=StoreSerializer()
    class Meta:
        model=BonMaintenance
        fields="__all__"
class ProduitsEnBonReformeSerializer(serializers.ModelSerializer):
    produit=ProductSerializer()
    class Meta:
        model=ProduitsEnBonReforme
        fields="__all__"

class BonReformeSerializer(serializers.ModelSerializer):
    produits=ProduitsEnBonReformeSerializer(source='produits_en_bon_reforme',many=True)
    entrepot=EntrepotSerializer()
    user=CustomUserSerializer()
    store=StoreSerializer()
    bonretour=BonRetourSerializer()
    class Meta:
        model=BonReforme
        fields="__all__"
class ProduitsEnBonEntrySerializer(serializers.ModelSerializer):
    stock=ProductSerializer()
    class Meta:
        model=ProduitsEnBonEntry
        fields="__all__"
class BonEntrySerializer(serializers.ModelSerializer):
    produits=ProduitsEnBonEntrySerializer(source="produits_en_bon_entry",many=True)
    fournisseur=FournisseurSerializer()
    entrepot=EntrepotSerializer()
    user=CustomUserSerializer()
    store=StoreSerializer()
    class Meta:
        model=BonEntry
        fields="__all__"
class ProduitsEnBonReintegrationSerializer(serializers.ModelSerializer):
    stock=ProductSerializer()
    class Meta:
        model=ProduitsEnBonReintegration
        fields="__all__"
class BonReintegrationSerializer(serializers.ModelSerializer):
    produits=ProduitsEnBonReintegrationSerializer(source="produits_en_bon_reintegration",many=True)
    bonRetour=BonRetourSerializer()
    entrepot=EntrepotSerializer()
    user=CustomUserSerializer()
    store=StoreSerializer()
    class Meta:
        model=BonReintegration
        fields="__all__"
class ProduitsEnBonSortieStockSerializer(serializers.ModelSerializer):
    stock=ProductSerializer()
    class Meta:
        model=ProduitsEnBonSortieStock
        fields="__all__"
class BonsortiedestockSerializer(serializers.ModelSerializer):
    produits=ProduitsEnBonSortieStockSerializer(source="produits_en_bon_sortie_stock",many=True)
    entrepot=EntrepotSerializer()
    user=CustomUserSerializer()
    store=StoreSerializer()
    bonL=BonSortieSerializer()
    Client=ClientSerializer()
    class Meta:
        model=Bonsortiedestock
        fields="__all__"
class ProduitsEnBonTransfertSerializer(serializers.ModelSerializer):
    stock_dep=StockSerializer()
    stock_arr=StockSerializer()
    class Meta:
        model=ProduitsEnBonTransfert
        fields="__all__"
class BonTransfertSerializer(serializers.ModelSerializer):
    produits=ProduitsEnBonTransfertSerializer(source="produits_en_bon_transfert",many=True)
    entrepot_depart=EntrepotSerializer()
    entrepot_arrive=EntrepotSerializer()
    user=CustomUserSerializer()
    store=StoreSerializer()
    class Meta:
        model=BonTransfert
        fields="__all__"





