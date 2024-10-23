from rest_framework import serializers
from .models import *
class EntrepotSerializer(serializers.ModelSerializer):
    class Meta:
        model=Entrepot
        fields="__all__"
class InventaireAnnuelSerializer(serializers.ModelSerializer):
    class Meta:
        model=InventaireAnnuel
        fields="__all__"
class BonRetourAncienSerializer(serializers.ModelSerializer):
    class Meta:
        model=BonRetourAncien
        fields="__all__"
class ProduitsEnBonRetourAncienSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitsEnBonRetourAncien
        fields="__all__"
class equipeInventaireSerializer(serializers.ModelSerializer):
    class Meta:
        model=equipeInventaire
        fields="__all__"
class produitEnInventaireAnnuelSerializer(serializers.ModelSerializer):
    class Meta:
        model=produitEnInventaireAnnuel
        fields="__all__"
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stock
        fields="__all__"
class BonTransfertMagasinSerializer(serializers.ModelSerializer):
    class Meta:
        model=BonTransfertMagasin
        fields="__all__"
class ProduitsEnBonTransfertMagSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitsEnBonTransfertMag
        fields="__all__"
class BonRetourSerializer(serializers.ModelSerializer):
    class Meta:
        model=BonRetour
        fields="__all__"
class BonEchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model=BonEchange
        fields="__all__"
class BonMaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=BonMaintenance
        fields="__all__"
class ProduitsEnBonMaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitsEnBonMaintenance
        fields="__all__"
class ProduitsEnBonEchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitsEnBonEchange
        fields="__all__"
class BonReformeSerializer(serializers.ModelSerializer):
    class Meta:
        model=BonReforme
        fields="__all__"
class ProduitsEnBonReformeSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitsEnBonReforme
        fields="__all__"
class BonEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model=BonEntry
        fields="__all__"
class BonReintegrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=BonReintegration
        fields="__all__"
class BonsortiedestockSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bonsortiedestock
        fields="__all__"
class BonTransfertSerializer(serializers.ModelSerializer):
    class Meta:
        model=BonTransfert
        fields="__all__"
class ProduitsEnBonRetourSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitsEnBonRetour
        fields="__all__"
class ProduitsEnBonTransfertSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitsEnBonTransfert
        fields="__all__"
class ProduitsEnBonEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitsEnBonEntry
        fields="__all__"
class ProduitsEnBonReintegrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitsEnBonReintegration
        fields="__all__"
class ProduitsEnBonSortieStockSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitsEnBonSortieStock
        fields="__all__"
