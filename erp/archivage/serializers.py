from rest_framework import serializers
from .models import *
from produits.serializers import *
from tiers.serializers import * 
from clientInfo.serializers import *
from reglements.serializers import *
from inventory.serializers import *
from user.serializers import *
class ArchivageProduitsEnBonSortieSerializer(serializers.ModelSerializer):
    stock=ProductSerializer()
    # entrepot=EntrepotSerializer()
    class Meta:
        model=ArchivageProduitsEnBonSortie
        fields="__all__"
class ArchivageBonSortieSerializer(serializers.ModelSerializer):
    produits=ArchivageProduitsEnBonSortieSerializer(many=True, source='produits_archivageBL')
    class Meta:
        model=ArchivageBonSortie
        fields="__all__"