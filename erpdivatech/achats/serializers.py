from rest_framework import serializers
from .models import *
class BonCommandeAchatSerializer(serializers.ModelSerializer):
    class Meta:
        model=BonCommandeAchat
        fields="__all__"
class ProduitsEnBonCommandesAchatSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitsEnBonCommandesAchat
        fields="__all__"
class DossierAchatSerializer(serializers.ModelSerializer):
    class Meta:
        model=DossierAchat
        fields="__all__"
class BonAchatSerializer(serializers.ModelSerializer):
    class Meta:
        model=BonAchat
        fields="__all__"
class FactureAchatSerializer(serializers.ModelSerializer):
    class Meta:
        model=FactureAchat
        fields="__all__"
class ProduitsEnFactureAchatSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitsEnFactureAchat
        fields="__all__"
class ProduitsEnBonAchatSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitsEnBonAchat
        fields="__all__"
class AvoirAchatSerializer(serializers.ModelSerializer):
    class Meta:
        model=AvoirAchat
        fields="__all__"
class BonReceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=BonReception
        fields="__all__"
class ExpeditionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Expedition
        fields="__all__"
class ProduitsEnBonReceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitsEnBonReception
        fields="__all__"
class ProjetCreditSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProjetCredit
        fields="__all__"
class CreditNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=CreditNote
        fields="__all__"
class ProduitsEnCreditNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitsEnCreditNote
        fields="__all__"
