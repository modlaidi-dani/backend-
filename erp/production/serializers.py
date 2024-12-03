from rest_framework import serializers
from .models import *
class ordreFabricationSerializer(serializers.ModelSerializer):
    class Meta:
        model=ordreFabrication
        fields="__all__"
class ProduitsEnOrdreFabricationSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitsEnOrdreFabrication
        fields="__all__"
class ProduitProductionBLSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitProductionBL
        fields="__all__"
class ProduitProductionFacSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitProductionFac
        fields="__all__"