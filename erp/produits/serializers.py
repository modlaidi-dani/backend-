from rest_framework import serializers
from .models import *
from clientInfo.serializers import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"
class ProductSerializer(serializers.ModelSerializer):
    stock=serializers.SerializerMethodField()
    quantity_globale=serializers.SerializerMethodField()
    price_revendeur=serializers.SerializerMethodField()
    price_clientfinal=serializers.SerializerMethodField()
    class Meta:
        model=Product
        fields="__all__"
    def get_stock(self,obj):
        from inventory.serializers import StockSerializer
        return StockSerializer(obj.mon_stock.all(),many=True).data
    def get_quantity_globale(self,obj):
        stocks=self.get_stock(obj)
        quantity_globale=0
        for stock in stocks:
            quantity = stock.get('quantity', 0)  
            quantity_globale += quantity 
        return quantity_globale
    def get_price_revendeur(self,obj):
        try:
            prices= obj.produit_var.filter(type_client__type_desc="Revendeur").first()
            return prices.prix_vente
        except:
            return obj.prix_vente   
    def get_price_clientfinal(self,obj):
        try:
            prices= obj.produit_var.filter(type_client__type_desc="Client Final").first()
            return prices.prix_vente
        except:
            return obj.prix_vente
        
        
class HistoriqueAchatProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model=HistoriqueAchatProduit
        fields="__all__"
class codeEASerializer(serializers.ModelSerializer):
    class Meta:
        model=codeEA
        fields="__all__"
class NumSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=NumSeries
        fields="__all__"
class variantsPrixClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=variantsPrixClient
        fields="__all__"
class PromotionSerializer(serializers.ModelSerializer):
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

