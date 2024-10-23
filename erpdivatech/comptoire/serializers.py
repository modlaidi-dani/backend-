from rest_framework import serializers
from .models import *
class pointVenteSerializer(serializers.ModelSerializer):
    class Meta:
        model=pointVente
        fields="__all__"
class EmplacementSerializer(serializers.ModelSerializer):
    class Meta:
        model=Emplacement
        fields="__all__"
class AffectationCaisseSerializer(serializers.ModelSerializer):
    class Meta:
        model=AffectationCaisse
        fields="__all__"
class ClotureSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cloture
        fields="__all__"
class BonComptoireSerializer(serializers.ModelSerializer):
    class Meta:
        model=BonComptoire
        fields="__all__"
class BonRectificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=BonRectification
        fields="__all__"
class verssementSerializer(serializers.ModelSerializer):
    class Meta:
        model=verssement
        fields="__all__"
class BonRetourComptoirSerializer(serializers.ModelSerializer):
    class Meta:
        model=BonRetourComptoir
        fields="__all__"
class ProduitsEnBonRetourComptoirSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitsEnBonRetourComptoir
        fields="__all__"
class ProduitsEnBonRectifSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitsEnBonRectif
        fields="__all__"
class ProduitsEnBonComptoirSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitsEnBonComptoir
        fields="__all__"
