from rest_framework import serializers
from .models import *
class MoyenTransportSerializer(serializers.ModelSerializer):
    class Meta:
        model=MoyenTransport
        fields="__all__"
class FicheLivraisonExterneSerializer(serializers.ModelSerializer):
    class Meta:
        model=FicheLivraisonExterne
        fields="__all__"
class requeteclientinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=requeteclientinfo
        fields="__all__"
class CourseLivraisonSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseLivraison
        fields="__all__"
class BlsEnRequeteClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlsEnRequeteClient
        fields="__all__"
class PreparationStockSerializer(serializers.ModelSerializer):
    class Meta:
        model=PreparationStock
        fields="__all__"
class BonTransportSerializer(serializers.ModelSerializer):
    class Meta:
        model=BonTransport
        fields="__all__"
class ProduitsEnBonTransportSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitsEnBonTransport
        fields="__all__"
class ReglementTransportSerializer(serializers.ModelSerializer):
    class Meta:
        model=ReglementTransport
        fields="__all__"
