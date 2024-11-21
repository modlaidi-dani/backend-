from rest_framework import serializers
from .models import *
class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model=store
        fields="__all__"

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Journal
        fields="__all__"

class PlanComptableClassSerializer(serializers.ModelSerializer):
    class Meta:
        model=PlanComptableClass
        fields="__all__"

class PlanComptableAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=PlanComptableAccount
        fields="__all__"

class CompteEntrepriseSerializer(serializers.ModelSerializer):
    class Meta:
        model=CompteEntreprise
        fields="__all__"

class TaxesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Taxes
        fields="__all__"

class DeviseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Devise
        fields="__all__"

class ValeurDeviseSerializer(serializers.ModelSerializer):
    class Meta:
        model=ValeurDevise
        fields="__all__"

class typeClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=typeClient
        fields="__all__"
        