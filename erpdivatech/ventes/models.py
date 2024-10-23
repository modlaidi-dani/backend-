from django.db import models
from django.contrib.auth.models import Permission
from user.models import CustomUser
from django.utils import timezone
from django.http import JsonResponse
from datetime import datetime
from django.db.models import Sum
from decimal import Decimal
from django.db.models import Sum, F, ExpressionWrapper, DecimalField
import ast

# class VentesCustomPermission(Permission):
#     class Meta:
#         verbose_name = 'Custom Permission'
#         verbose_name_plural = 'Custom Permissions'

class validationBl(models.Model):
    type_validation = models.CharField(max_length=25, default='', blank=True, null=True )
    percentage =  models.DecimalField(max_digits=15, decimal_places=2, default=0)
    codeBl = models.CharField(max_length=25, default='', blank=True, null=True )
    montantBl = models.DecimalField(max_digits=150, decimal_places=2, default=0)
    solde_note = models.DecimalField(max_digits=150, decimal_places=2, default=0)
    user = models.ForeignKey(CustomUser,on_delete = models.CASCADE, related_name='mes_validation', blank=True, null=True, default=None)
    client_name =  models.CharField(max_length=25, default='', blank=True, null=True )

class BonSortie(models.Model):
    Reglement_etat_CHOICES = [
        ("non-regle", "non-regle"),
        ("regle", "regle"),     
    ]
    idBon = models.CharField(
          ("id Bon"), 
          max_length=200,
          blank=False,
          null=False,
          unique=False
    )    
    dateBon =models.DateField()
    client =models.ForeignKey('tiers.Client',on_delete = models.CASCADE, related_name='client_bonS')
    totalPrice = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    user =models.ForeignKey(CustomUser,on_delete = models.CASCADE, related_name='mes_bons', blank=True)
    entrepot = models.ForeignKey('inventory.Entrepot', on_delete=models.CASCADE,related_name='entrepot_bons', default=None, blank=True, null=True)
    mode_reglement = models.ForeignKey('reglements.ModeReglement', on_delete = models.CASCADE, related_name='bonL_reglements_type', null=True, blank=True, default=None)
    echeance_reglement = models.ForeignKey('reglements.EcheanceReglement', on_delete = models.CASCADE, related_name='bonL_reglements_echeance', null=True, blank=True, default=None)
    banque_Reglement = models.ForeignKey('tiers.Banque', on_delete=models.CASCADE, related_name='banque_reglements_bonL', blank=True, null=True, default=None )
    num_cheque_reglement = models.CharField(max_length=2500 , default="", null=True, blank =True)
    Remise = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    agenceLivraison = models.CharField(max_length=2500 , default="", null=True, blank =True)
    fraisLivraison = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    fraisLivraisonexterne = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    note = models.TextField(default="")
    valide = models.BooleanField(default=False)
    ferme =  models.BooleanField(default=False)
    modifiable = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=True)
    livre = models.BooleanField(default=False)
    typebl = models.CharField(max_length=200, blank=True, null=True, default='')
    reference_pc = models.CharField(max_length=200, blank=True, null=True, default='') 
    name_pc = models.CharField(max_length=200, blank=True, null=True, default='') 
    store = models.ForeignKey('clientinfo.store', on_delete = models.CASCADE, related_name='bonL_store', null=True, blank=True, default=None)
    

    
    def __str__(self):
	    return "Bon no: " + str(self.idBon) + "CLient store: " + str(self.client.store.id) +  "BL Store : " + str(self.store.id)
    

class DemandeTransfert(models.Model):
    BonSNo = models.ForeignKey(BonSortie, on_delete = models.CASCADE, related_name='demande_sortie_transfert')
    BonTransfert = models.ForeignKey('inventory.BonTransfert', on_delete = models.CASCADE, related_name='demande_transfert')
    etat = models.CharField(max_length=150, default='', blank=True, null=True)
    
class ConfirmationBl(models.Model):
    BonNo = models.ForeignKey(BonSortie, on_delete = models.CASCADE, related_name='confrimation_bon')
    dateConfirmation =models.DateTimeField()
    dateLivraisonPrevu=models.DateField()
    fichier_confirmation = models.FileField(upload_to="media/document")
    
class ProduitsEnBonSortie(models.Model):
    BonNo = models.ForeignKey(BonSortie, on_delete = models.CASCADE, related_name='produits_en_bon_sorties')
    stock = models.ForeignKey('produits.Product', on_delete = models.CASCADE, related_name='bons_sortie')
    kit = models.TextField(default="")
    quantity = models.IntegerField(default=1)
    unitprice = models.DecimalField(max_digits=15, decimal_places=2)
    totalprice = models.DecimalField(max_digits=15, decimal_places=2)   
    entrepot = models.ForeignKey('inventory.Entrepot', on_delete = models.CASCADE, related_name='mesproduit_bons_sortie', default=None, blank=True, null=True)
    def __str__(self):
	    return "Bon no: " + str(self.BonNo.idBon) + ", Item = " + self.stock.name

        
class BonGarantie(models.Model):
    idBon = models.CharField(
          ("id Bon"), 
          max_length=200,
          blank=False,
          null=False,
          unique=True
    )    
    dateBon = models.DateField()
    bonLivraisonAssocie = models.ForeignKey(BonSortie, on_delete = models.CASCADE, related_name='bon_garantie',  null=True, blank=True, default=None)
    store = models.ForeignKey('clientinfo.store', on_delete=models.CASCADE, null=True, blank=True, default=None)
    client = models.ForeignKey('tiers.Client', on_delete=models.CASCADE, null=True, blank=True, default=None)
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name='mes_bons_garantie', blank=True, null=True, default=None)
    tps_ecoule =   models.CharField( max_length=200, blank=True, null=True, default="" )    
    def get_mystore(self):
        my_products= self.produits_en_bon_garantie.all()
        for product in my_products:
            store= product.stock_dep.entrepot.store
            return store
        
    def __str__(self):
	    return "Bon no: " + str(self.idBon)
       
class ProduitsEnBonGarantie(models.Model):
    BonNo = models.ForeignKey(BonGarantie, on_delete = models.CASCADE, related_name='produits_en_bon_garantie')
    produit = models.ForeignKey('produits.Product', on_delete = models.CASCADE, related_name='mes_bons_garantie')
    quantity = models.IntegerField(default=1)
    livre = models.BooleanField(default=False)
    NumeroSeries = models.TextField(default="") 
    

    def __str__(self):
	    return "Bon no: " + str(self.BonNo.idBon) + ", Item = " + self.produit.name 
 
class BonDevis(models.Model):
    idBon = models.CharField(
          ("id Bon"), 
          max_length=200,
          blank=False,
          null=False,
          unique=True
    )    
    dateBon =models.DateField()
    client =models.ForeignKey('tiers.Client',on_delete = models.CASCADE, related_name='client_bonS_devis')
    user =models.ForeignKey(CustomUser,on_delete = models.CASCADE, related_name='mes_bons_devis',blank=True, null=True, default=None)
    store = models.ForeignKey('clientinfo.store', on_delete=models.CASCADE, null=True, blank=True, default=None)

    def __str__(self):
	    return "Bon no: " + str(self.idBon)

    
   
class ProduitsEnBonDevis(models.Model):
    BonNo = models.ForeignKey(BonDevis, on_delete = models.CASCADE, related_name='produits_en_bon_devis')
    produit = models.ForeignKey('produits.Product', on_delete = models.CASCADE, related_name='mes_bons_devis')    
    totalPrice = models.DecimalField(max_digits=15, decimal_places=2)
    UnitPrice = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.IntegerField(default=1)
  
    def __str__(self):
	    return "Bon no: " + str(self.BonNo.idBon) + ", Item = " + self.produit.name   
 
class BonCommande(models.Model):
    idBon = models.CharField(
          ("id Bon"), 
          max_length=200,
          blank=False,
          null=False,
          unique=True
    )    
    dateBon =models.DateField(default=datetime.now)
    date_reglement = models.DateField(default=datetime.now)
    client =models.ForeignKey('tiers.Client',on_delete = models.CASCADE, related_name='client_bonS_commande')
    mode_reglement = models.ForeignKey('reglements.ModeReglement', on_delete = models.CASCADE, related_name='commande_reglements_type')
    echeance_reg = models.ForeignKey('reglements.EcheanceReglement', on_delete=models.CASCADE)
    valide = models.BooleanField(default=False)
    ferme =  models.BooleanField(default=False)
    regle = models.BooleanField(default=False)
    user =models.ForeignKey(CustomUser,on_delete = models.CASCADE, related_name='mes_bons_commande',blank=True, null=True, default=None)
    store = models.ForeignKey('clientinfo.store', on_delete=models.CASCADE, null=True, blank=True, default=None)

    def __str__(self):
	    return "Bon no: " + str(self.idBon)  
  
class ProduitsEnBonCommande(models.Model):
    BonNo = models.ForeignKey(BonCommande, on_delete = models.CASCADE, related_name='produits_en_bon_commande')
    produit = models.ForeignKey('produits.Product', on_delete = models.CASCADE, related_name='mes_bons_commande')
    unit_price = models.DecimalField(max_digits=15, decimal_places=2)
    totalPrice = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.IntegerField(default=1)

class Facture(models.Model):
    Reglement_etat_CHOICES = [
        ("en Attente", "en Attente"),
        ("Règlement Reçu", "Règlement Reçu"),
        ("Expédié", "Expédié"),
        ("Facture", "Facture"),
        ("Facture Comptabilisé", "Facture Comptabilisé"),
    ]
    codeFacture = models.CharField( max_length=200,blank=False,null=False,unique=True)  
    date_facture = models.DateField()
    date_reglement = models.DateField(default=datetime.now)
    client = models.ForeignKey('tiers.Client', on_delete = models.CASCADE, related_name='client_facture')
    store = models.ForeignKey('clientinfo.store', on_delete=models.CASCADE, null=True, blank=True, default=None)
    BonS = models.ForeignKey(BonSortie, on_delete = models.CASCADE, related_name='bonS_facture', default=None, blank=True, null=True)
    mode_reglement = models.ForeignKey('reglements.ModeReglement', on_delete = models.CASCADE, related_name='facture_reglements_type', null=True, blank=True, default=None)
    echeance_reglement = models.ForeignKey('reglements.EcheanceReglement', on_delete = models.CASCADE, related_name='facture_reglements_echeance', null=True, blank=True, default=None)
    banque_Reglement = models.ForeignKey('tiers.Banque', on_delete=models.CASCADE, related_name='banque_reglements', blank=True, null=True, default=None )
    num_cheque_reglement = models.CharField(max_length=2500 , default="", null=True, blank =True)
    Remise = models.CharField(max_length=20,null=True, blank=True, default='')
    etat_reglement = models.CharField( max_length=30, choices=Reglement_etat_CHOICES) 
    shippingCost = models.DecimalField(max_digits=15, decimal_places=2 , null=True, blank=True)
    totalPrice = models.IntegerField(default=0)
    valide = models.BooleanField(default=False)
    ferme =  models.BooleanField(default=False)
    regle = models.BooleanField(default=False)


class AvoirVente(models.Model):
    BonSortieAssocie = models.ForeignKey(BonSortie, on_delete = models.CASCADE, related_name='avoirs_bonsortie')
    client = models.ForeignKey('tiers.Client', on_delete = models.CASCADE, related_name='avoirs_client')
    codeAvoir = models.CharField(  max_length=200,blank=False,null=False)   
    dateEmission = models.DateField(default=datetime.now)
    motif =  models.CharField(  max_length=200,blank=False,null=False, default="")
    montant = models.CharField(  max_length=200,blank=False,null=False, default="")
    store = models.ForeignKey('clientinfo.store', on_delete=models.CASCADE,blank=True , null=True, default=None)  

class ProduitsEnFacture(models.Model):
    FactureNo = models.ForeignKey(Facture, on_delete = models.CASCADE, related_name='produits_en_facture')
    stock = models.ForeignKey('produits.Product', on_delete = models.CASCADE, related_name='facture')
    quantity = models.IntegerField(default=0)
    unitprice = models.DecimalField(max_digits=15, decimal_places=2,default=0,null=True)
    totalprice = models.DecimalField(max_digits=15, decimal_places=2 ,default=0,null=True)  

    def __str__(self):
	    return "Facture no: " + str(self.FactureNo.codeFacture) + ", Item = " + self.stock.name