from django.db import models
from clientinfo.models import store, typeClient
from user.models import CustomUser
from django.contrib.auth.models import Permission
# from achats.models import BonAchat,FactureAchat
# from reglements.models import ReglementFournisseur
from decimal import Decimal
import ast

# class TiersCustomPermission(Permission):
#     class Meta:
#         verbose_name = 'Custom Permission'
#         verbose_name_plural = 'Custom Permissions'

class Banque(models.Model):
    nom  = models.CharField(max_length=2500 , default="", null=True, blank =True) 
    code  = models.CharField(max_length=2500 , default="", null=True, blank =True) 
    bic  = models.CharField(max_length=2500 , default="", null=True, blank =True) 
    actif = models.BooleanField(default=True)
    store = models.ForeignKey(store, on_delete=models.CASCADE, related_name='banque_store', blank=True, null=True, default=None)

class Agence(models.Model):
    banque = models.ForeignKey(Banque,on_delete = models.CASCADE, related_name='banque_agence', default=None, null=True, blank =True) 
    code  = models.CharField(max_length=2500 , default="", null=True, blank =True) 
    adresse = models.CharField(max_length=2500 , default="", null=True, blank =True) 
    actif = models.BooleanField(default=True) 
    store = models.ForeignKey(store, on_delete=models.CASCADE, related_name='agence_store', blank=True, null=True, default=None)
     
class Fournisseur(models.Model):
    fournisseur_Type_CHOICES = [
        ("PME", "PME"),
        ("Institutionnel", "Institutionnel"),
        ("Automobile", "Automobile"),
        ("Revendeur", "Revendeur"),
        ("BTPH", "BTPH"),
        ("Industrie", "Industrie"),
        ("Autre", "Autre"),
    ]
    codeFournisseur =models.CharField(max_length=25)
    acronym = models.CharField(max_length=150)
    raison_Social = models.CharField(max_length=150)
    adresse = models.CharField(max_length=250, default="")
    phone = models.CharField(max_length=150, default="")
    email = models.CharField(max_length=150, default="")
    typefournisseur = models.CharField( max_length=25, choices=fournisseur_Type_CHOICES, default="Autre")   
    fournisseurEtrange = models.BooleanField()
    fournisseurClient = models.CharField(max_length=150, default="")
    store = models.ForeignKey(store, on_delete=models.CASCADE, related_name='fournisseur_store', blank=True, null=True, default=None)
    

    def __str__(self):
	    return "fournisseur : " + str(self.acronym)
 
class Region(models.Model):
    label = models.CharField(max_length=250, default="", null=True, blank=True)
    wilayas = models.TextField(blank=True, null=True,)
    store = models.ForeignKey('clientinfo.store', on_delete=models.CASCADE, related_name="mes_regions", null=True, blank=True)
    date_created = models.DateTimeField() 
    
    def getClients(self):
        wilayas_list = ast.literal_eval(self.wilayas)
        return Client.objects.filter(region_client__in=wilayas_list, store__id = 1)

    
class Client(models.Model):
    name = models.CharField(max_length=150)
    adresse = models.CharField(max_length=250, default="")
    phone = models.CharField(max_length=150, default="")
    email = models.CharField(max_length=150, default="")
    sourceClient = models.CharField(max_length=150, default="")
    categorie_client = models.ForeignKey(typeClient, on_delete = models.CASCADE, related_name='clients_type', blank=True, null=True, default=None)
    registreCommerce = models.CharField(max_length=150, default="")
    Nif = models.CharField(max_length=150, default="")
    Nis = models.CharField(max_length=150, default="")
    num_article = models.CharField(max_length=150, default="")
    region_client = models.CharField(max_length=150, default="")
    solde = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    store = models.ForeignKey(store, on_delete=models.CASCADE, related_name='client_store', blank=True, null=True, default=None)
    user = models.ForeignKey(CustomUser,on_delete = models.CASCADE, related_name='mes_clients', blank=True, null=True, default=None)
    valide  = models.BooleanField(default=True)
    NisDoc = models.FileField(upload_to="media/document")
    NifDoc = models.FileField(upload_to="media/document")
    RCDoc = models.FileField(upload_to="media/document")
    AIDoc = models.FileField(upload_to="media/document")
    def __str__(self):
	    return "CLient : " + str(self.name) +  "Store : " + str(self.store.id)

class ProspectionClient(models.Model):
    client = models.ForeignKey(Client,on_delete = models.CASCADE, related_name='ma_prospection', blank=True, null=True, default=None)
    SourceClient  = models.CharField(max_length=250, default="", null=True, blank=True)
    etatProspection = models.CharField(max_length=250, default="", null=True, blank=True)
   

class Tentatives(models.Model):
    propspection = models.ForeignKey(ProspectionClient,on_delete = models.CASCADE, related_name='mes_tentative', blank=True, null=True, default=None)  
    user = models.ForeignKey(CustomUser,on_delete = models.CASCADE, related_name='mes_tentatives', blank=True, null=True, default=None)
    dateDebutTentative = models.DateTimeField()
    dateFinTentative = models.DateTimeField()
    MoyenContact = models.CharField(max_length=250, default="", null=True, blank=True)
    note = models.CharField(max_length=250, default="", null=True, blank=True)
    
class CompteBancaire(models.Model):
    client = models.ForeignKey(Client,on_delete = models.CASCADE, related_name='compte_bancaire_client', blank=True, null=True, default=None)
    fournisseur = models.ForeignKey(Fournisseur,on_delete = models.CASCADE, related_name='compte_bancaire_client', blank=True, null=True, default=None)
    labelCompte = models.CharField(max_length=250, default="", null=True, blank=True)
    Banque = models.ForeignKey(Banque, on_delete=models.CASCADE, related_name='compte_banque_client', blank=True, null=True, default=None)
    Agence = models.ForeignKey(Agence, on_delete=models.CASCADE, related_name='compte_banque_client', blank=True, null=True, default=None)
    TypeCompte= models.TextField(blank=True, null=True)
    compteclient=models.TextField(blank=True, null=True)
    num_compte = models.IntegerField(null=True, blank=True)
    cle=models.IntegerField(null=True, blank=True)
    IBAN=models.IntegerField(null=True, blank=True)
                                