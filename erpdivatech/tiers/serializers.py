from rest_framework import serializers
from .models import *
class BanqueSerializer(serializers.ModelSerializer):
    class Meta:
        model=Banque
        fields="__all__"
class AgenceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Agence
        fields="__all__"
class FournisseurSerializer(serializers.ModelSerializer):
    class Meta:
        model=Fournisseur
        fields="__all__"
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Region
        fields="__all__"
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields="__all__"
class ProspectionClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProspectionClient
        fields="__all__"
class TentativesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tentatives
        fields="__all__"
class CompteBancaireSerializer(serializers.ModelSerializer):
    class Meta:
        model=CompteBancaire
        fields="__all__"
