from rest_framework import serializers
from .models import *
        
class ProduitsEnBonCommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitsEnBonCommande
        fields="__all__"
class FactureSerializer(serializers.ModelSerializer):
    class Meta:
        model=Facture
        fields="__all__"
class AvoirVenteSerializer(serializers.ModelSerializer):
    class Meta:
        model=AvoirVente
        fields="__all__"
class validationBlSerializer(serializers.ModelSerializer):
    class Meta:
        model=validationBl
        fields="__all__"
class BonSortieSerializer(serializers.ModelSerializer):
    class Meta:
        model=BonSortie
        fields="__all__"
class DemandeTransfertSerializer(serializers.ModelSerializer):
    class Meta:
        model=DemandeTransfert
        fields="__all__"
class ConfirmationBlSerializer(serializers.ModelSerializer):
    class Meta:
        model=ConfirmationBl
        fields="__all__"
class ProduitsEnBonSortieSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitsEnBonSortie
        fields="__all__"
class BonGarantieSerializer(serializers.ModelSerializer):
    class Meta:
        model=BonGarantie
        fields="__all__"
class ProduitsEnBonGarantieSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitsEnBonGarantie
        fields="__all__"
class BonDevisSerializer(serializers.ModelSerializer):
    class Meta:
        model=BonDevis
        fields="__all__"
class ProduitsEnBonDevisSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitsEnBonDevis
        fields="__all__"
class BonCommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model=BonCommande
        fields="__all__"
class ProduitsEnFactureSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitsEnFacture
        fields="__all__"