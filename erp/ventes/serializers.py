from rest_framework import serializers
from .models import *
from produits.serializers import *
from tiers.serializers import * 
from clientInfo.serializers import *
from reglements.serializers import *
from inventory.serializers import *
from user.serializers import *
class ProduitsEnBonCommandeSerializer(serializers.ModelSerializer):
    produit=ProductSerializer()
    class Meta:
        model=ProduitsEnBonCommande
        fields="__all__"
class ProduitsEnBonSortieSerializer(serializers.ModelSerializer):
    stock=ProductSerializer()
    # entrepot=EntrepotSerializer()
    class Meta:
        model=ProduitsEnBonSortie
        fields="__all__"
class BonSortieSerializer(serializers.ModelSerializer):
    produits=ProduitsEnBonSortieSerializer(many=True, source='produits_en_bon_sorties')
    user=CustomUserSerializer()
    client=ClientSerializer()
    entrepot=serializers.SerializerMethodField()
    confirmationFile=serializers.SerializerMethodField()
    confirmationDateTime=serializers.SerializerMethodField()
    ValidatePar=serializers.SerializerMethodField()
    statebill=serializers.SerializerMethodField()
    total_price=serializers.SerializerMethodField()
    total_avoir=serializers.SerializerMethodField()
    garantieprepared=serializers.SerializerMethodField()
    my_tax=serializers.SerializerMethodField()
    references=serializers.SerializerMethodField()
    designations=serializers.SerializerMethodField()
    etat_transfert=serializers.SerializerMethodField()
    price_annule=serializers.SerializerMethodField()
    total_soldprice=serializers.SerializerMethodField()
    total_paid_amount=serializers.SerializerMethodField()
    total_remaining_amount=serializers.SerializerMethodField()
    regle=serializers.SerializerMethodField()
    caisseBons=serializers.SerializerMethodField()
    ma_marge=serializers.SerializerMethodField()
    
    
    class Meta:
        model=BonSortie
        fields="__all__"
    def get_entrepot(self, obj):
        from inventory.serializers import EntrepotSerializer
        entrepot= EntrepotSerializer(obj.entrepot).data
        return entrepot
    def get_confirmationFile(self,obj):
        if len(obj.confrimation_bon.all()) > 0:
            return obj.confrimation_bon.first().fichier_confirmation.url
        else:
            return ''
        
    def get_confirmationDateTime(self,obj):
        if len(obj.confrimation_bon.all()) > 0:
            return obj.confrimation_bon.first().dateConfirmation
        else:
            return ''
        
    def get_ValidatePar(self,obj):
        validation_object = validationBl.objects.filter(codeBl = obj.idBon).first()
        if validation_object is not None:
            return validation_object.user.username
        else: 
            return ''
        
    def get_statebill(self,obj):
        if len(obj.bon_garantie.all()) == 0 and len(obj.bonsL_transports.all()) == 0:
            return 'attente-prep'
        elif len(obj.bon_garantie.all()) > 0 and len(obj.bonsL_transports.all()) == 0:   
            return 'prep-nonliv' 
        elif len(obj.bon_garantie.all()) == 0 and len(obj.bonsL_transports.all()) > 0:   
            return 'liv-nonprep' 
        elif len(obj.bon_garantie.all()) > 0 and len(obj.bonsL_transports.all()) > 0:   
            return 'livre' 
        
    def get_total_avoir(self,obj):
        total_avoir = 0
        try:
            avoirs=obj.avoirs_bonsortie.all()
            for avoir in avoirs:
                total_avoir += Decimal(avoir.montant) * Decimal('1.19')
        except:
            total_avoir=total_avoir
        return total_avoir
        
    def get_total_price(self,obj):
        price_part = obj.produits_en_bon_sorties.aggregate(total_price=Sum('totalprice'))['total_price']
        total_price = float(price_part) if price_part is not None else float(0)
        
        return total_price
    
    def get_garantieprepared(self,obj):
        return len(obj.bon_garantie.all()) > 0
    
    def get_my_tax(self,obj):
        tax = 0
        for produit in obj.produits_en_bon_sorties.all():
            tax += (produit.stock.tva_douan * produit.quantity)
        return round(tax,2)  
    
    def get_references(self,obj):
        if obj.reference_pc != '':
            result_list = []
            if "[" in str(obj.reference_pc):
                result_list = ast.literal_eval(obj.reference_pc)
                return result_list
            else:
                result_list.append(obj.reference_pc)
                return result_list
        else:
            return []
    
    def get_designations(self,obj):
        result_list = []
        if obj.name_pc != '':
            if "[" in str(obj.name_pc):
                result_list = ast.literal_eval(obj.name_pc)
                return result_list
            else:
                result_list.append(obj.name_pc)
                return result_list
        else:
            return []
        
    def get_etat_transfert(self,obj):
        mon_etat = DemandeTransfert.objects.filter(BonSNo=obj).first()
        if mon_etat is not None:
            return mon_etat.etat.lower() == 'true'
        else:
            return True
         
    def get_price_annule(self,obj):
        if len(obj.MesbonRetours.all())>0:
            filtered_bons_retour = [bon for bon in obj.MesbonRetours.filter(valide=True) if bon.reintegrated]
            result_sum = sum(Decimal(bon.total_price_retour) * Decimal(1.19) for bon in filtered_bons_retour)
            return result_sum
        else:
            return 0
        
    def get_total_soldprice(self,obj):
        price_part = obj.produits_en_bon_sorties.aggregate(total_price=Sum('totalprice'))['total_price']

        if price_part is not None:
            total_price = round((price_part - Decimal(obj.Remise)) * Decimal('1.19') , 2)
            return round(total_price, 2) if total_price is not None else 0.00
        else:
            return 0.00

    def get_total_paid_amount(self,obj):
        return sum(reglement.montant for reglement in obj.bonS_reglements.all())

    def get_total_remaining_amount(self,obj):
        # Assuming get_total_price is a Decimal field
        total_price = Decimal(self.get_total_price(obj))
        remise = Decimal(obj.Remise)
        total_paid_amount = Decimal(self.get_total_paid_amount(obj))

        return  round(((total_price - remise) * Decimal('1.19')) - total_paid_amount, 2)

    def get_regle(self,obj):
       return round(self.get_total_soldprice(obj),0) == round(self.get_total_paid_amount(obj),0)
       
    def get_caisseBons(self,obj):
        reglements = sum(reglement.montant for reglement in obj.bonS_reglements.all())
        caisse = None
        if reglements != 0 :
            caisse = obj.bonS_reglements.first().CompteEntreprise
            return caisse
        
    def get_ma_marge(self,obj):
        # All products in the current BonSortie
        products = obj.produits_en_bon_sorties.all()
        
        # Set to hold all products from BonRetours linked to the current BonSortie
        excluded_products = set()

        # Find all products in ProduitsEnBonRetour where the BonRetour is linked to the current BonSortie
        related_bon_retours = obj.MesbonRetours.all()
        for bon_retour in related_bon_retours:
            for product in bon_retour.produits_en_bon_retour.all():
                excluded_products.add(product.produit.id)  # Store product ids to be excluded

        margin = 0
        for p in products:
            # Only include in margin calculation if not in excluded_products
            if p.stock.id not in excluded_products:
                margin += ((p.stock.prix_vente - p.stock.prix_achat) * p.quantity)
        
        return round(margin, 2)
    
class ProduitsEnFactureSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitsEnFacture
        fields="__all__"
class FactureSerializer(serializers.ModelSerializer):
    produits=ProduitsEnFactureSerializer(many=True, source='produits_en_facture')
    client=ClientSerializer()
    store=StoreSerializer()
    BonS=BonSortieSerializer()
    mode_reglement=ModeReglementSerializer()
    echeance_reglement=EcheanceReglementSerializer()
    banque_Reglement=BanqueSerializer()
    class Meta:
        model=Facture
        fields="__all__"
class produitsEnAvoirSerializer(serializers.ModelSerializer):
    produit=ProduitsEnBonSortieSerializer()
    class Meta:
        model=produitsEnAvoir
        fields="__all__"
class produitsEnAvoirASerializer(serializers.ModelSerializer):
    class Meta:
        model=produitsEnAvoirA
        fields="__all__"
class AvoirVenteAncienSerializer(serializers.ModelSerializer):
    produits=produitsEnAvoirASerializer(many=True,source="produits_en_avoirA")
    class Meta:
        model=AvoirVenteAncien
        fields="__all__"
class AvoirVenteSerializer(serializers.ModelSerializer):
    produits=produitsEnAvoirSerializer(many=True, source="produits_en_avoir")
    BonSortieAssocie=BonSortieSerializer()
    client=ClientSerializer()
    store=StoreSerializer()
    class Meta:
        model=AvoirVente
        fields="__all__"
class validationBlSerializer(serializers.ModelSerializer):
    user=CustomUserSerializer()
    class Meta:
        model=validationBl
        fields="__all__"

class DemandeTransfertSerializer(serializers.ModelSerializer):
    BonSNo=BonSortieSerializer()
    # BonTransfert=BonTransfertSerializer()
    class Meta:
        model=DemandeTransfert
        fields="__all__"
class ConfirmationBlSerializer(serializers.ModelSerializer):
    BonNo=BonSortieSerializer()
    class Meta:
        model=ConfirmationBl
        fields="__all__"
class ProduitsEnBonGarantieSerializer(serializers.ModelSerializer):
    produit=ProductSerializer()
    class Meta:
        model=ProduitsEnBonGarantie
        fields="__all__"
class BonGarantieSerializer(serializers.ModelSerializer):
    produits=ProduitsEnBonGarantieSerializer(many=True,source='produits_en_bon_garantie')
    bonLivraisonAssocie=BonSortieSerializer()
    client=ClientSerializer()
    store=StoreSerializer()
    user=CustomUserSerializer()
    class Meta:
        model=BonGarantie
        fields="__all__"

class ProduitsEnBonDevisSerializer(serializers.ModelSerializer):
    produit=ProductSerializer()
    class Meta:
        model=ProduitsEnBonDevis
        fields="__all__"
class BonDevisSerializer(serializers.ModelSerializer):
    produits=ProduitsEnBonDevisSerializer(many=True,source='produits_en_bon_devis')
    client=ClientSerializer()
    store=StoreSerializer()
    user=CustomUserSerializer()
    class Meta:
        model=BonDevis
        fields="__all__"

class BonCommandeSerializer(serializers.ModelSerializer):
    produits=ProduitsEnBonCommandeSerializer(many=True,source='produits_en_bon_commande')
    client=ClientSerializer()
    store=StoreSerializer()
    user=CustomUserSerializer()
    mode_reglement=ModeReglementSerializer()
    echeance_reg=EcheanceReglementSerializer()
    class Meta:
        model=BonCommande
        fields="__all__"
