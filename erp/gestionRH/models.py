from django.db import models
from datetime import datetime, time, date
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta
import calendar


class RequeteSalarie(models.Model):
    date = models.DateTimeField(default=datetime.now)
    objet = models.CharField(max_length=255, default='')
    message = models.TextField(default='')
    reponse = models.TextField(default='') 
    datereponse = models.DateTimeField(default=datetime.now)
    destinataire = models.CharField(max_length=255, default='')
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, default=None, null=True, blank=True)
    store = models.ForeignKey('clientinfo.store', on_delete=models.CASCADE, default=None, null=True, blank=True) 

class Event(models.Model):
    name = models.CharField(max_length=100, help_text="The name of the event.")
    description = models.TextField(default='', help_text="The name of the event.")
    event_date = models.DateField(help_text="The date of the event.")
    remember_months = models.IntegerField(
        default=0,
        help_text="Number of months in advance to remember the event."
    )
    remind_days_before = models.IntegerField(
        default=0,
        help_text="Number of days before the event to send a reminder."
    )

    def __str__(self):
        return f"{self.name} on {self.event_date}"

        
class Salarie(models.Model):
    nom = models.CharField(max_length=255, default='')
    nomarabe = models.CharField(max_length=255, default='')
    fonction = models.CharField(max_length=255, default='')
    fonctionarabe = models.CharField(max_length=255, default='')
    email = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=255, default='')
    ccp = models.CharField(max_length=255, default='')
    association = models.CharField(max_length=255, default='')
    actif = models.BooleanField(default=True)
    num_assurancesocial = models.CharField(max_length=255, default='')
    datenaiss = models.DateTimeField(auto_now_add=False, default=datetime.now)
    lieu_naissance = models.CharField(max_length=255, default='')
    lieu_naissancearabe = models.CharField(max_length=255, default='')
    echellon = models.CharField(max_length=255, default='')
    degre = models.CharField(max_length=255, default='')
    cout_heure = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    salaire = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    prime_espece = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, default=None, null=True, blank=True)
    store = models.ForeignKey('clientinfo.store', on_delete=models.CASCADE, default=None, null=True, blank=True)
    dateDebut = models.DateField(help_text="The date of start.", default=datetime.now)
    dateEnd = models.DateField(help_text="The date of start.", default=datetime.now)
        
class ReglementCompte(models.Model):
    salarie = models.ForeignKey(Salarie, on_delete= models.CASCADE, related_name="mes_reglementscompte", null=True, blank = True, default=None)
    dateSortie = models.DateTimeField(auto_now_add=False)
    montant = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    note = models.TextField(default='') 
    
class Conge(models.Model):
    salarie = models.ForeignKey(Salarie, on_delete= models.CASCADE, null=True,related_name="mon_conge", blank = True, default=None)
    dateDebut = models.DateTimeField(default=datetime.now)
    dateFin = models.DateTimeField(default=datetime.now)
    type_conge = models.TextField(default="")
    nbrJourPris = models.IntegerField(default='0')

        
    def __str__(self):
        return f'Salarie {self.salarie.nom} - Date: {self.dateDebut.strftime("%Y-%m-%d")}'
    
    
class Pointage(models.Model):
    salarie = models.ForeignKey(Salarie, on_delete= models.CASCADE, null=True,related_name="mon_pointage", blank = True, default=None)
    date = models.DateTimeField(default=datetime.now)
    temps_arrive = models.TimeField(default='09:00:00')
    temps_depart = models.TimeField(default='17:00:00')
    
    def __str__(self):
        return f'Salarie {self.salarie.nom} - Date: {self.date.strftime("%Y-%m-%d")}'

class AvanceSalaire(models.Model):
    date = models.DateTimeField(auto_now_add=False)
    salarie = models.ForeignKey(Salarie, on_delete= models.CASCADE, related_name="mes_avances_salaire", null=True, blank = True, default=None)
    motif = models.CharField(max_length=255, default='') 
    montant = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class PrixSocial(models.Model):
    date = models.DateTimeField(auto_now_add=False)
    salarie = models.ForeignKey(Salarie, on_delete= models.CASCADE, related_name="mes_prox_social", null=True, blank = True, default=None)
    motif = models.CharField(max_length=255, default='') 
    montanttotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    montantperMonth = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    nombre_months = models.CharField(max_length=255, default='')
    

        
class HeureSup(models.Model):
    nombre_heure = models.CharField(max_length=255, default='')
    date = models.DateTimeField(auto_now_add=True)
    datetimedeb = models.DateTimeField(default=datetime.now)
    datetimeend = models.DateTimeField(default=datetime.now)
    salarie = models.ForeignKey(Salarie, on_delete= models.CASCADE, related_name="mes_heure_sup", null=True, blank = True, default=None)
    motif = models.CharField(max_length=255, default='') 
    valide = models.BooleanField(default=True)
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, default=None, null=True, blank=True)
    store = models.ForeignKey('clientinfo.store', on_delete=models.CASCADE, default=None, null=True, blank=True)
    
class PrimeMotivation(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    salarie = models.ForeignKey(Salarie, on_delete= models.CASCADE, related_name="mes_primesmotivation", null=True, blank = True, default=None)
    motif = models.CharField(max_length=255, default='') 
    valide = models.BooleanField(default=True)
    montant = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    viremenet = models.BooleanField(default=True)
    
class Absence(models.Model):
    date = models.DateTimeField(auto_now_add=False)
    salarie = models.ForeignKey(Salarie, on_delete= models.CASCADE, related_name="mes_absences", null=True, blank = True, default=None)
    nombre_heure = models.CharField(max_length=255, default='')
    motif = models.CharField(max_length=255, default='') 
    minusSource = models.CharField(max_length=255, default='') 
    justifie = models.BooleanField(default=False)
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, default=None, null=True, blank=True)
    store = models.ForeignKey('clientinfo.store', on_delete=models.CASCADE, default=None, null=True, blank=True)
    
class Contrat(models.Model):
    salarie = models.ForeignKey(Salarie, on_delete= models.CASCADE, related_name="ma_contrat", null=True, blank = True, default=None)
    numero_contrat = models.CharField(max_length=255, default='')
    numero_decision_recrutement = models.CharField(max_length=255, default='')
    numero_pv_installation = models.CharField(max_length=255, default='')
    datedeb = models.DateTimeField(default=datetime.now)
    datesignature = models.DateTimeField(default=datetime.now)
    datefin = models.DateTimeField(default=datetime.now)
    type_contrat = models.CharField(max_length=255, default='')

class Renumeration(models.Model):
   mois = models.CharField(max_length=255, default='')
   salarie = models.ForeignKey(Salarie, on_delete= models.CASCADE, null=True, blank = True, default=None)
   virement_valide = models.BooleanField(default=False)

class BoiteArchive(models.Model):
   date = models.DateTimeField(auto_now_add=True)
   date_facturation_fournisseur = models.DateTimeField(auto_now_add=False)
   date_facturation_transitaire = models.DateTimeField(auto_now_add=False)
   montant = models.DecimalField(max_digits=35, decimal_places=2, default=0)
   typedocument  = models.CharField(max_length=255, default='')
   label  = models.CharField(max_length=255, default='')
   document = models.FileField(upload_to="media/document") 