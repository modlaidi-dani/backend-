from rest_framework import serializers
from .models import *
class ModeReglementSerializer(serializers.ModelSerializer):
    class Meta:
        model=ModeReglement
        fields="__all__"
class depenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=depense
        fields="__all__"
class TypeDepenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=TypeDepense
        fields="__all__"
class EcheanceReglementSerializer(serializers.ModelSerializer):
    class Meta:
        model=EcheanceReglement
        fields="__all__"
class HistoriqueMontantRecupererSerializer(serializers.ModelSerializer):
    class Meta:
        model=HistoriqueMontantRecuperer
        fields="__all__"
class ReglementSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reglement
        fields="__all__"
class ReglementFournisseurSerializer(serializers.ModelSerializer):
    class Meta:
        model=ReglementFournisseur
        fields="__all__"
class ClotureReglementsSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClotureReglements
        fields="__all__"
class montantCollectedSerializer(serializers.ModelSerializer):
    class Meta:
        model=montantCollected
        fields="__all__"
class mouvementCaisseSerializer(serializers.ModelSerializer):
    class Meta:
        model=mouvementCaisse
        fields="__all__"
