from rest_framework import serializers
from .models import *
class RequeteSalarieSerializer(serializers.ModelSerializer):
    class Meta:
        model=RequeteSalarie
        fields="__all__"
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields="__all__"
class SalarieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Salarie
        fields="__all__"
class ReglementCompteSerializer(serializers.ModelSerializer):
    class Meta:
        model=ReglementCompte
        fields="__all__"
class CongeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Conge
        fields="__all__"
class PointageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pointage
        fields="__all__"
class AvanceSalaireSerializer(serializers.ModelSerializer):
    class Meta:
        model=AvanceSalaire
        fields="__all__"
class PrixSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model=PrixSocial
        fields="__all__"
class HeureSupSerializer(serializers.ModelSerializer):
    class Meta:
        model=HeureSup
        fields="__all__"
class PrimeMotivationSerializer(serializers.ModelSerializer):
    class Meta:
        model=PrimeMotivation
        fields="__all__"
class AbsenceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Absence
        fields="__all__"
class ContratSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contrat
        fields="__all__"
class RenumerationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Renumeration
        fields="__all__"
class BoiteArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model=BoiteArchive
        fields="__all__"
