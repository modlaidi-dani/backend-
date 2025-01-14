from rest_framework import serializers
from .models import *
from inventory.serializers import *
from produits.models import *
class ProduitsEnOrdreFabricationSerializer(serializers.ModelSerializer):
    stock=ProductSerializer()
    class Meta:
        model=ProduitsEnOrdreFabrication
        fields="__all__"
class ordreFabricationSerializer(serializers.ModelSerializer):
    produits=ProduitsEnOrdreFabricationSerializer(many=True,source="produits_en_ordre_fabrication")
    entrepot_destocker=EntrepotSerializer()
    entrepot_stocker=EntrepotSerializer()
    pc_created=ProductSerializer()
    class Meta:
        model=ordreFabrication
        fields="__all__"

class ProduitProductionBLSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitProductionBL
        fields="__all__"
class ProduitProductionFacSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitProductionFac
        fields="__all__"