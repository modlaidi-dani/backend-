from django.db import models
from user.models import CustomUser
from django.contrib.auth.models import Permission
import json
from decimal import Decimal
# Create your models here.
# class ComptoirCustomPermission(Permission):
#     class Meta:
#         verbose_name = 'Custom Permission'
#         verbose_name_plural = 'Custom Permissions'
        
class pointVente(models.Model):
    label = models.CharField(max_length=200)
    entrepot = models.ForeignKey('inventory.Entrepot',on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='mes_points_ventes')
    type_reglement = models.CharField(max_length=200)
    mode_payment = models.ForeignKey('reglements.ModeReglement', on_delete=models.CASCADE , blank=True, null=True, related_name="pointVentes")
    adresse=models.TextField(blank=True, null=True, default="")
    Téléphone = models.TextField(blank=True, null=True, default="")
    fidelite = models.BooleanField(default=True)
    store = models.ForeignKey('clientinfo.store',on_delete=models.CASCADE, default=None, null=True, blank=True)
    
class Emplacement(models.Model):
    Label = models.TextField(blank=True, null=True, default="")
    lieu = models.TextField(blank=True, null=True, default="")   
    store = models.ForeignKey('clientinfo.store',on_delete=models.CASCADE, default=None, null=True, blank=True)
    
class AffectationCaisse(models.Model):
    emplacement =models.ForeignKey(pointVente, on_delete=models.CASCADE, related_name="pos_affectation", blank=True, null=True, default=None)
    CompteTres = models.ForeignKey('clientinfo.CompteEntreprise', on_delete=models.CASCADE, blank=True, null=True, default=None)
    utilisateur = models.ForeignKey('user.CustomUser' , on_delete=models.CASCADE ,  related_name="mon_affectation", blank=True, null=True, default=None)
    store = models.ForeignKey('clientinfo.store',on_delete=models.CASCADE, default=None, null=True, blank=True)

class Cloture(models.Model):
    montant= models.CharField(max_length=100, blank=True, null=True, default='')
    date = models.DateField()  
    utilisateur= models.ForeignKey('user.CustomUser',on_delete=models.CASCADE, blank=True, null=True, default=None)
    collected = models.BooleanField(default=False)
    store= models.ForeignKey('clientinfo.store',on_delete=models.CASCADE, blank=True, null=True, default=None)
    
class BonComptoire(models.Model):
    idBon = models.CharField(
          ("id Bon"), 
          max_length=200,
          blank=False,
          null=False,
          unique=True
    )    
    dateBon = models.DateField()
    pointVente = models.ForeignKey(pointVente, on_delete=models.CASCADE, blank=True, null=True, default=None)
    caisse = models.ForeignKey('clientinfo.CompteEntreprise', on_delete=models.CASCADE, blank=True, null=True, default=None)
    observation = models.CharField(
          max_length=4500,
          blank=True,
          null=True,
          default=''
    )  
    totalprice = models.DecimalField(max_digits=15, decimal_places=2,null=True, blank=True, default=0)
    totalremise = models.DecimalField(max_digits=15, decimal_places=2 ,null=True, blank=True, default=0)
    store = models.ForeignKey('clientinfo.store', on_delete=models.CASCADE, related_name="bons_comptoir_store", null=True, blank=True, default=None)
    client = models.ForeignKey('tiers.Client', related_name="mesbons_comptoir",on_delete=models.CASCADE, null=True, blank=True, default=None)
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name='mes_bons_comptoire',blank=True, null=True, default=None)


    
class BonRectification(models.Model):
    idBon = models.CharField(
          ("id Bon"), 
          max_length=200,
          blank=False,
          null=False,
          unique=True
    )    
    dateBon = models.DateField()
    pointVente = models.ForeignKey(pointVente, on_delete=models.CASCADE, blank=True, null=True, default=None)
    caisse = models.ForeignKey('clientinfo.CompteEntreprise', on_delete=models.CASCADE, blank=True, null=True, default=None)
    observation = models.CharField(
          max_length=4500,
          blank=True,
          null=True,
          default=''
    )  
    totalprice = models.DecimalField(max_digits=15, decimal_places=2,null=True, blank=True, default=0)
    totalremise = models.DecimalField(max_digits=15, decimal_places=2 ,null=True, blank=True, default=0)
    store = models.ForeignKey('clientinfo.store', on_delete=models.CASCADE, related_name="bons_rectif_store", null=True, blank=True, default=None)
    client = models.ForeignKey('tiers.Client', related_name="mesbons_rectification",on_delete=models.CASCADE, null=True, blank=True, default=None)
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name='mes_bons_rectification',blank=True, null=True, default=None)


    
class verssement(models.Model):
    montant= models.CharField(max_length=100, blank=True, null=True, default='')
    date = models.DateField()  
    utilisateur= models.ForeignKey('user.CustomUser',on_delete=models.CASCADE, blank=True, null=True, default=None)
    bon_comptoir_associe = models.ForeignKey(BonComptoire, on_delete = models.CASCADE,  blank=True, null=True, default=None, related_name='verssements')
    bon_rectification_associe = models.ForeignKey(BonRectification, on_delete = models.CASCADE,  blank=True, null=True, default=None ,related_name='verssements')
    store= models.ForeignKey('clientinfo.store',on_delete=models.CASCADE, blank=True, null=True, default=None)
    
    def __str__(self):
	    return "Verssement de : " + str(self.montant) + ", POUR BON NO: = " + str(self.bon_comptoir_associe.idBon)
	    

            
class BonRetourComptoir(models.Model):
    idBon = models.CharField(
          ("id Bon"), 
          max_length=200,
          blank=False,
          null=False,
          unique=True
    )    
    dateBon = models.DateField()
    client = models.ForeignKey('tiers.Client', related_name="bonsretour_compt", on_delete=models.CASCADE, null=True, blank=True, default=None)
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name='mes_bons_retourcomptoire', blank=True, null=True, default=None)
    bon_comptoir_associe = models.ForeignKey(BonComptoire, on_delete = models.CASCADE, related_name='bons_retour_compt', blank=True, null=True, default=None)
    bon_rectification_associe = models.ForeignKey(BonRectification, on_delete = models.CASCADE, related_name='bons_retour_compt', blank=True, null=True, default=None)
    decision = models.CharField( max_length=200,blank=False,null=False, default='')

    

class ProduitsEnBonRetourComptoir(models.Model):
    BonNo = models.ForeignKey(BonRetourComptoir, on_delete = models.CASCADE, related_name='produits_en_bon_retourcomptoir')
    produit = models.ForeignKey('produits.Product', on_delete = models.CASCADE, related_name='mes_bons_retourcomptoir')    
    totalprice = models.DecimalField(max_digits=15, decimal_places=2)
    unitprice = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.IntegerField(default=1)
      
class ProduitsEnBonRectif(models.Model):
    BonNo = models.ForeignKey(BonRectification, on_delete = models.CASCADE, related_name='produits_en_bon_rectification')
    stock = models.ForeignKey('produits.Product', on_delete = models.CASCADE, related_name='bons_rectif')
    entrepot = models.ForeignKey('inventory.Entrepot',on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='produit_rectification')
    quantity = models.IntegerField(default=1)
    unitprice = models.DecimalField(max_digits=15, decimal_places=2)
    totalprice = models.DecimalField(max_digits=15, decimal_places=2)  
    
class ProduitsEnBonComptoir(models.Model):
    BonNo = models.ForeignKey(BonComptoire, on_delete = models.CASCADE, related_name='produits_en_bon_comptoir')
    stock = models.ForeignKey('produits.Product', on_delete = models.CASCADE, related_name='bons_comptoir')
    entrepot = models.ForeignKey('inventory.Entrepot',on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='produit_boncomp')
    quantity = models.IntegerField(default=1)
    unitprice = models.DecimalField(max_digits=15, decimal_places=2)
    totalprice = models.DecimalField(max_digits=15, decimal_places=2)  