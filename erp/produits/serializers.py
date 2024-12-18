from rest_framework import serializers
from .models import *
from clientInfo.serializers import *
from produits.serializers import *

class CategorySerializer(serializers.ModelSerializer):
    store=StoreSerializer()
    class Meta:
        model=Category
        fields="__all__"
class ProductSerializer(serializers.ModelSerializer):
    category=CategorySerializer()
    store=StoreSerializer()
    class Meta:
        model=Product
        fields="__all__"
class HistoriqueAchatProduitSerializer(serializers.ModelSerializer):
    produit=ProductSerializer()
    class Meta:
        model=HistoriqueAchatProduit
        fields="__all__"
class codeEASerializer(serializers.ModelSerializer):
    produit=ProductSerializer()
    class Meta:
        model=codeEA
        fields="__all__"
class NumSeriesSerializer(serializers.ModelSerializer):
    produit=ProductSerializer()
    class Meta:
        model=NumSeries
        fields="__all__"
class variantsPrixClientSerializer(serializers.ModelSerializer):
    produit=ProductSerializer()
    type_client=typeClientSerializer()
    class Meta:
        model=variantsPrixClient
        fields="__all__"
class PromotionSerializer(serializers.ModelSerializer):
    produit=ProductSerializer()
    type_client=typeClientSerializer()
    class Meta:
        model=Promotion
        fields="__all__"
class Variantes_productSerializer(serializers.ModelSerializer):
    class Meta:
        model=Variantes_product
        fields="__all__"
class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductVariant
        fields="__all__"
class VerificationArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model=VerificationArchive
        fields="__all__"
class historique_prix_achatSerializer(serializers.ModelSerializer):
    class Meta:
        model=historique_prix_achat
        fields="__all__"
class ListProductVerificationArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model=ListProductVerificationArchive
        fields="__all__"

