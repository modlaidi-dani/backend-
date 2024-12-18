from rest_framework import serializers
from .models import *
from clientInfo.serializers import *
from tiers.serializers import *
from user.serializers import *
from ventes.serializers import *
from inventory.serializers import *
from produits.serializers import *





class MoyenTransportSerializer(serializers.ModelSerializer):
    store=StoreSerializer()
    class Meta:
        model=MoyenTransport
        fields="__all__"
class FicheLivraisonExterneSerializer(serializers.ModelSerializer):
    class Meta:
        model=FicheLivraisonExterne
        fields="__all__"
class requeteclientInfoSerializer(serializers.ModelSerializer):
    chauffeur=CustomUserSerializer()
    moyen_transport=MoyenTransportSerializer()
    bonlivraison=BonSortieSerializer()
    class Meta:
        model=requeteclientInfo
        fields="__all__"
class CourseLivraisonSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseLivraison
        fields="__all__"
class BlsEnRequeteClientSerializer(serializers.ModelSerializer):
    requete=requeteclientInfoSerializer()
    bonlivraison=BonSortieSerializer()
    class Meta:
        model=BlsEnRequeteClient
        fields="__all__"
class PreparationStockSerializer(serializers.ModelSerializer):
    bonEntry=BonEntrySerializer()
    class Meta:
        model=PreparationStock
        fields="__all__"
class ProduitsEnBonTransportSerializer(serializers.ModelSerializer):
    produit=ProductSerializer()
    class Meta:
        model=ProduitsEnBonTransport
        fields="__all__"
class BonTransportSerializer(serializers.ModelSerializer):
    produit=ProduitsEnBonTransportSerializer(many=True,source="produits_en_bon_transport")
    bonlivraison=BonSortieSerializer()
    moyen_transport=MoyenTransportSerializer()
    client=ClientSerializer()
    store=StoreSerializer()
    user=CustomUserSerializer()
    regle=serializers.SerializerMethodField()
    formatted_date=serializers.SerializerMethodField()
    produits_livre=serializers.SerializerMethodField()
    class Meta:
        model=BonTransport
        fields="__all__" 
    def get_regle(self,obj):
        if len(obj.reglements_bontransport.all()) > 0:
            return True
        else:
            return False
    def get_formatted_date(self,obj):
        return obj.date_depart.strftime('%d/%m/%Y')
        
    def get_produits_livre(self,obj):
        produits_bon_sortie = obj.bonlivraison.produits_en_bon_sorties.all()

        # Create a dictionary to store quantities for each product
        quantities = {produit_en_bon_sortie.obj.id: {'qty_in_bonTr': 0, 'qty_inBonL': 0, 'produit_ref': produit_en_bon_sortie.stock.reference} for produit_en_bon_sortie in produits_bon_sortie}

        # Calculate quantities in BonTransport and BonSortie
        if len(obj.produits_en_bon_transport.all()) > 0:
            for produit_en_bon_transport in obj.produits_en_bon_transport.all():
                produit_id = produit_en_bon_transport.produit.id
                produit_ref = produit_en_bon_transport.produit.reference
                quantities[produit_id]['qty_in_bonTr'] += produit_en_bon_transport.quantity

            for produit_en_bon_sortie in produits_bon_sortie:
                produit_id = produit_en_bon_sortie.stock.id
                quantities[produit_id]['qty_inBonL'] += produit_en_bon_sortie.quantity

            # Create a list of products with quantities
            result = [{'product': qty['produit_ref'], 'qty_in_bonTr': qty['qty_in_bonTr'], 'qty_inBonL': qty['qty_inBonL']} for produit_id, qty in quantities.items()]
            return result
        else:
            return []
class ReglementTransportSerializer(serializers.ModelSerializer):
    bon_transport=BonTransportSerializer()
    store=StoreSerializer()
    user=CustomUserSerializer()
    class Meta:
        model=ReglementTransport
        fields="__all__"
