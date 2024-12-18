from rest_framework import serializers
from .models import *
from user.serializers import *
from clientInfo.serializers import *
class RequeteSalarieSerializer(serializers.ModelSerializer):
    user=CustomUserSerializer()
    store=StoreSerializer()
    class Meta:
        model=RequeteSalarie
        fields="__all__"
class EventSerializer(serializers.ModelSerializer):
    reminder_date=serializers.SerializerMethodField()
    next_remember_date=serializers.SerializerMethodField()
    class Meta:
        model=Event
        fields="__all__"
    def get_reminder_date(self,obj):
        return obj.event_date - timedelta(days=obj.remind_days_before)

    def get_next_remember_date(self,obj):
        return obj.event_date - timedelta(days=30 * obj.remember_months)
class SalarieSerializer(serializers.ModelSerializer):
    user=CustomUserSerializer()
    store=StoreSerializer()
    total_valid_Supphours=serializers.SerializerMethodField()
    total_late_days=serializers.SerializerMethodField()
    total_daysnopoint=serializers.SerializerMethodField()
    total_avances=serializers.SerializerMethodField()
    total_prixsocial=serializers.SerializerMethodField()
    total_absent_days=serializers.SerializerMethodField()
    total_absent_Hours=serializers.SerializerMethodField()
    class Meta:
        model=Salarie
        fields="__all__"  
    def get_total_valid_Supphours(self,obj):
        return obj.mes_heure_sup.filter(valide=True).aggregate(Sum('nombre_heure'))['nombre_heure__sum'] or 0
    
    def get_total_late_days(self,obj):
        return obj.get_late_minutes / 480
    
    
    def get_total_daysnopoint(self,obj):
       return len(obj.mon_pointage.filter(temps_arrive=time(0, 0, 0)))
    
    def get_total_avances(self,obj):
        return obj.mes_avances_salaire.filter(date__month=2).aggregate(Sum('montant'))['montant__sum'] or 0
    
    
    def get_total_prixsocial(self,obj):
        return obj.mes_prox_social.all().aggregate(Sum('montantperMonth'))['montantperMonth__sum'] or 0
    
    
    def get_total_absent_days(self,obj):
        return len(obj.mes_absences.filter(date__month=2)) - len(obj.mes_absences.filter(justifie = True, date__month=2))
    
    
    def get_total_absent_Hours(self,obj):
        if obj.get_total_absent_days>0:
           return  obj.mes_absences.filter(justifie=False, date__month=2).aggregate(Sum('nombre_heure'))['nombre_heure__sum'] or 0
        else:
            return 0     
            

class ReglementCompteSerializer(serializers.ModelSerializer):
    salarie=SalarieSerializer()
    class Meta:
        model=ReglementCompte
        fields="__all__"
class CongeSerializer(serializers.ModelSerializer):
    salarie=SalarieSerializer()
    NbrJour=serializers.SerializerMethodField()
    class Meta:
        model=Conge
        fields="__all__"
    def get_NbrJour(self,obj):
        return (obj.dateFin - obj.dateDebut).days + 1
class PointageSerializer(serializers.ModelSerializer):
    salarie=SalarieSerializer()
    class Meta:
        model=Pointage
        fields="__all__"
class AvanceSalaireSerializer(serializers.ModelSerializer):
    salarie=SalarieSerializer()
    class Meta:
        model=AvanceSalaire
        fields="__all__"
class PrixSocialSerializer(serializers.ModelSerializer):
    salarie=SalarieSerializer()
    end_month=serializers.SerializerMethodField()
    class Meta:
        model=PrixSocial
        fields="__all__"
    def get_end_month(self,obj):
        end_date = obj.date + timedelta(days=int(int(obj.nombre_months) + 1) * 30)
        current_date = datetime.now()
        return end_date.replace(day=obj.date.day)
class HeureSupSerializer(serializers.ModelSerializer):
    salarie=SalarieSerializer()
    user=CustomUserSerializer()
    store=StoreSerializer()
    class Meta:
        model=HeureSup
        fields="__all__"
class PrimeMotivationSerializer(serializers.ModelSerializer):
    salarie=SalarieSerializer()
    class Meta:
        model=PrimeMotivation
        fields="__all__"
class AbsenceSerializer(serializers.ModelSerializer):
    salarie=SalarieSerializer()
    user=CustomUserSerializer()
    store=StoreSerializer()
    class Meta:
        model=Absence
        fields="__all__"
class ContratSerializer(serializers.ModelSerializer):
    salarie=SalarieSerializer()
    class Meta:
        model=Contrat
        fields="__all__"
class RenumerationSerializer(serializers.ModelSerializer):
    salarie=SalarieSerializer()
    class Meta:
        model=Renumeration
        fields="__all__"
class BoiteArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model=BoiteArchive
        fields="__all__"
