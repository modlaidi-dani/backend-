from rest_framework import serializers
from .models import *
from tiers.serializers import * 
from django.db.models import Sum,DecimalField
from comptoire.models import BonRetourComptoir
from django.db.models.functions import Coalesce
from decimal import Decimal

class StoreSerializer(serializers.ModelSerializer):
    total_bon_price=serializers.SerializerMethodField()
    bons_counts_per_month=serializers.SerializerMethodField()
    total_retours_per_month=serializers.SerializerMethodField()
    class Meta:
        model=store
        fields="__all__"
    def get_total_bon_price(self, obj):
        total_bon_sortie_price = obj.bonL_store.aggregate(total=Coalesce(Sum('totalPrice'), 0, output_field=DecimalField()))['total']
        total_bon_comptoir_price = obj.bons_comptoir_store.aggregate(total=Coalesce(Sum('totalprice'), 0, output_field=DecimalField()))['total']
        retour_comptoirs = BonRetourComptoir.objects.filter(bon_comptoir_associe__store=obj)
        total_price_rembourse = sum(retour_comptoir.myTotalPrice for retour_comptoir in retour_comptoirs)
        return round(Decimal((total_bon_sortie_price + total_bon_comptoir_price) - total_price_rembourse),0)

    def get_bons_counts_per_month(self, obj):
        bons_per_month = []
        for month in range(1, 13):
            bons_comptoire_count = obj.bons_comptoir_store.filter(
                dateBon__month=month
            ).count()
            bons_sortie_count = obj.bonL_store.filter(
                dateBon__month=month
            ).count()
            total_bons_count = bons_comptoire_count + bons_sortie_count
            bons_per_month.append(total_bons_count)
        return bons_per_month
    def get_total_retours_per_month(self, obj):
        retours_per_month = []
        for month in range(1, 13):
            retours_count = BonRetourComptoir.objects.filter(
                bon_comptoir_associe__store=obj,
                dateBon__month=month
            ).count()
            retours_count = BonRetourComptoir.objects.filter(
                bon_comptoir_associe__store=obj,
                dateBon__month=month
            ).count()
            retours_per_month.append(retours_count)

        return retours_per_month

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
    banque=BanqueSerializer()
    agence=AgenceSerializer()
    compteComptable=PlanComptableAccountSerializer()
    store=StoreSerializer()
    mon_credit=serializers.SerializerMethodField()
    mon_debit=serializers.SerializerMethodField()
    class Meta:
        model=CompteEntreprise
        fields="__all__"
    def get_mon_credit(self,obj):
        credit_by_date = []
        if len(obj.mouvements_sortie.all())>0:
            for bon in obj.mouvements_sortie.all():            
                date_str = bon.date.strftime("%Y-%m-%d")
                prix_payed_float = float(bon.credit)

                # Check if both dateReglement and caisse already exist in the list
                entry_exists = any(
                    entry['dateBon'] == date_str 
                    for entry in credit_by_date
                )

                if entry_exists:
                    # Update the existing entry with the sum of prix_payed
                    for entry in credit_by_date:
                        if entry['dateBon'] == date_str :
                            entry['montant'] += prix_payed_float
                            break
                else:
                    # Add a new entry to the list
                    credit_by_date.append({'dateBon': date_str, 'montant': prix_payed_float})
        return credit_by_date 
    def mon_debit(self,obj):
        credit_by_date = []
        if len(obj.mouvements_recu.all())>0:
            for bon in obj.mouvements_recu.all():            
                date_str = bon.date.strftime("%Y-%m-%d")
                prix_payed_float = float(bon.credit)

                # Check if both dateReglement and caisse already exist in the list
                entry_exists = any(
                    entry['dateBon'] == date_str 
                    for entry in credit_by_date
                )

                if entry_exists:
                    # Update the existing entry with the sum of prix_payed
                    for entry in credit_by_date:
                        if entry['dateBon'] == date_str :
                            entry['montant'] += prix_payed_float
                            break
                else:
                    # Add a new entry to the list
                    credit_by_date.append({'dateBon': date_str, 'montant': prix_payed_float})
        return credit_by_date  
class TaxesSerializer(serializers.ModelSerializer):
    store=StoreSerializer()
    class Meta:
        model=Taxes
        fields="__all__"

class DeviseSerializer(serializers.ModelSerializer):
    store=StoreSerializer()
    class Meta:
        model=Devise
        fields="__all__"

class ValeurDeviseSerializer(serializers.ModelSerializer):
    Devise=DeviseSerializer()
    store=StoreSerializer()
    class Meta:
        model=ValeurDevise
        fields="__all__"

class typeClientSerializer(serializers.ModelSerializer):
    store=StoreSerializer()
    class Meta:
        model=typeClient
        fields="__all__"
        