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
    client=ClientSerializer()
    mode_reglement=ModeReglementSerializer()
    echeance_reglement=EcheanceReglementSerializer()
    # entrepot=EntrepotSerializer()
    banque_Reglement=BanqueSerializer()
    store=StoreSerializer()
    class Meta:
        model=BonSortie
        fields="__all__"
class ProduitsEnFactureSerializer(serializers.ModelSerializer):
    stock=ProductSerializer()
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
class AvoirVenteSerializer(serializers.ModelSerializer):
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
    client=ClientSerializer()
    store=StoreSerializer()
    user=CustomUserSerializer()
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
