from rest_framework import serializers
from .models import *
from tiers.serializers import *  
from inventory.serializers import *  
from clientInfo.serializers import *  
from reglements.serializers import *  
from user.serializers import *  
from produits.serializers import *
from reglements.serializers import *

class ProduitsEnBonCommandesAchatSerializer(serializers.ModelSerializer):
    produit=ProductSerializer()
    class Meta:
        model=ProduitsEnBonCommandesAchat
        fields="__all__"

class BonCommandeAchatSerializer(serializers.ModelSerializer):
    produit=ProduitsEnBonCommandesAchatSerializer(many=True)
    fournisseur=FournisseurSerializer()
    livraison=EntrepotSerializer()
    mode_reglement=ModeReglementSerializer()
    echeance_reglement=EcheanceReglementSerializer()
    monnaie=ValeurDeviseSerializer()
    user=CustomUserSerializer()
    store=StoreSerializer()

    class Meta:
        model=BonCommandeAchat
        fields="__all__"

class DossierAchatSerializer(serializers.ModelSerializer):
    fournisseur=FournisseurSerializer()
    BonCommande=BonCommandeAchatSerializer()
    banque_Reglement=BanqueSerializer()
    user=CustomUserSerializer()
    store=StoreSerializer()
    class Meta:
        model=DossierAchat
        fields="__all__"
class ProduitsEnBonAchatSerializer(serializers.ModelSerializer):
    produit=ProductSerializer()
    class Meta:
        model=ProduitsEnBonAchat
        fields="__all__"
class BonAchatSerializer(serializers.ModelSerializer):
    produit=ProduitsEnBonAchatSerializer(many=True)
    fournisseur=FournisseurSerializer()
    entrepot=EntrepotSerializer()
    monnaie=ValeurDeviseSerializer()
    mode_reglement=ModeReglementSerializer()
    echeance_reglement=EcheanceReglement()
    user=CustomUserSerializer()
    store=StoreSerializer()
    total_paid_amount=serializers.SerializerMethodField()
    total_remaining_amount=serializers.SerializerMethodField()
    class Meta:
        model=BonAchat
        fields="__all__"
    def get_total_paid_amount(self, obj):
        return sum(reglement.montant for reglement in obj.bonAchats_reglements.all())
    def get_total_remaining_amount(self, obj):
        total_paid = self.get_total_paid_amount(obj)  
        return obj.totalPrice - total_paid
class ProduitsEnFactureAchatSerializer(serializers.ModelSerializer):
    stock=ProductSerializer()
    class Meta:
        model=ProduitsEnFactureAchat
        fields="__all__"
class FactureAchatSerializer(serializers.ModelSerializer):
    prduits=ProduitsEnFactureAchatSerializer(many=True)
    fournisseur=FournisseurSerializer()
    livraison=EntrepotSerializer()
    BonAchat=BonAchatSerializer()
    mode_reglement=ModeReglementSerializer()
    echeance_reglement=EcheanceReglement()
    monnaie=ValeurDeviseSerializer()
    user=CustomUserSerializer()
    store=StoreSerializer()
    total_price=serializers.SerializerMethodField()
    class Meta:
        model=FactureAchat
        fields="__all__"
    def get_total_price(self, obj):
        total_price = obj.prduits.aggregate(total_price=Sum('totalprice'))['total_price']
        return round(total_price, 2) if total_price is not None else 0.00

class AvoirAchatSerializer(serializers.ModelSerializer):
    fournisseur=FournisseurSerializer()
    store=StoreSerializer() 
    class Meta:
        model=AvoirAchat
        fields="__all__"
class ExpeditionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Expedition
        fields="__all__"
class ProduitsEnBonReceptionSerializer(serializers.ModelSerializer):
    produit=ProductSerializer()
    class Meta:
        model=ProduitsEnBonReception
        fields="__all__"
class BonReceptionSerializer(serializers.ModelSerializer):
    produit=ProduitsEnBonReceptionSerializer(many=True)
    entrepot=EntrepotSerializer()
    expedition=ExpeditionSerializer()
    unite_monitaire=ValeurDeviseSerializer()
    user=CustomUserSerializer()
    store=StoreSerializer()
    class Meta:
        model=BonReception
        fields="__all__"


class ProjetCreditSerializer(serializers.ModelSerializer):
    user=CustomUserSerializer()
    store=StoreSerializer()
    class Meta:
        model=ProjetCredit
        fields="__all__"
class ProduitsEnCreditNoteSerializer(serializers.ModelSerializer):
    produit=ProductSerializer()
    class Meta:
        model=ProduitsEnCreditNote
        fields="__all__"
class CreditNoteSerializer(serializers.ModelSerializer):
    produit=ProduitsEnCreditNoteSerializer(many=True)
    BonAchat=BonAchatSerializer()
    Projet=ProjetCreditSerializer()
    user=CustomUserSerializer()
    store=StoreSerializer()
    class Meta:
        model=CreditNote
        fields="__all__"

