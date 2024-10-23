from django.db import models
from clientinfo.models import store
from user.models import CustomUser
from tiers.models import Client
from django.contrib.auth.models import Permission
# from comptoire.models import ProduitsEnBonComptoir, ProduitsEnBonRetourComptoir, BonComptoire
# from ventes.models import ProduitsEnBonSortie
from decimal import Decimal
# Create your models here.
from django.db.models import Q
from django.db.models import F

# class InventoryCustomPermission(Permission):
#     class Meta:
#         verbose_name = 'Custom Permission'
#         verbose_name_plural = 'Custom Permissions'

class Entrepot(models.Model): 
   store = models.ForeignKey(store,on_delete=models.CASCADE, related_name='store_entrepot', blank=True, null=True, default=None)
   name= models.CharField(max_length=100)
   adresse = models.CharField(max_length=100 , default="", null=True, blank=True)
   ville = models.CharField(max_length=100)
   codePostal = models.CharField(max_length=100 , default="", null=True, blank=True)
   phone = models.CharField(max_length=100, default="", null=True, blank=True)
   def __str__(self) :
         return self.name


class InventaireAnnuel(models.Model):
    codeInv = models.CharField(max_length=100)
    dateInv = models.DateField()
    datecloture = models.DateField()
    note = models.TextField()
    entrepot = models.ForeignKey(Entrepot, on_delete=models.CASCADE, related_name="entrepot_inventaire", blank =False, null=False)
    store =models.ForeignKey(store,on_delete = models.CASCADE, related_name='store_inventaires')

class BonRetourAncien(models.Model):
    idBon = models.CharField(
          ("id Bon"), 
          max_length=200,
          blank=False,
          null=False,
          unique=True
    )    
    dateBon = models.DateField()
    totalPrice = models.IntegerField(default=0)
    bonL =  models.CharField(max_length=100)
    entrepot = models.ForeignKey(Entrepot, on_delete = models.CASCADE, related_name='entrepot_retourancien', blank=True, null=True, default = None) 
    client =  models.CharField(max_length=100)
    valide = models.BooleanField(blank=True, null=True, default=False)
    store =models.ForeignKey(store,on_delete = models.CASCADE, related_name='store_bons_retour_ancien')
    user =models.ForeignKey(CustomUser,on_delete = models.CASCADE, related_name='mes_bons_retour_ancien', blank=True, null=True, default=None)
    def __str__(self):
	    return "Bon no: " + str(self.idBon)

class ProduitsEnBonRetourAncien(models.Model):
    BonNo = models.ForeignKey(BonRetourAncien, on_delete = models.CASCADE, related_name='produits_en_bon_retourancien')
    referenceproduit = models.CharField(max_length=100)    
    nomproduit = models.CharField(max_length=100)  
    totalprice = models.DecimalField(max_digits=15, decimal_places=2)
    unitprice = models.DecimalField(max_digits=15, decimal_places=2)
    reintegrated = models.BooleanField(default=False)
    image = models.FileField(upload_to="media/document") 
    warranty = models.BooleanField(default=False)
    numseries = models.CharField( 
          max_length=200,
          blank=True,
          null=True,
          default = '',  
    )    
    quantity = models.IntegerField(default=1)
  
    def __str__(self):
	    return "Bon no: " + str(self.BonNo.idBon) + ", Item = " + self.nomproduit  	    

class equipeInventaire(models.Model):
    inv_annuel = models.ForeignKey(InventaireAnnuel, on_delete=models.CASCADE, related_name="inventaire_assosiated", blank =False, null = False)
    label_equipe = models.TextField()

class produitEnInventaireAnnuel(models.Model):
    Equipe = models.ForeignKey(equipeInventaire, on_delete=models.CASCADE, related_name="liste_produits")
    product = models.ForeignKey('produits.Product', on_delete=models.CASCADE, related_name='mon_inventaire')
    quantity = models.PositiveIntegerField(default=0)  
    
class Stock(models.Model):
    product = models.ForeignKey('produits.Product', on_delete=models.CASCADE, related_name='mon_stock')
    entrepot = models.ForeignKey(Entrepot, on_delete=models.CASCADE, related_name="inventories")
    quantity = models.PositiveIntegerField(default=0)
    quantity_initial = models.PositiveIntegerField(default=0)
    quantity_pc = models.PositiveIntegerField(default=0)
    quantity_kit = models.PositiveIntegerField(default=0)
    quantity_blocked = models.PositiveIntegerField(default=0)

class BonTransfertMagasin(models.Model):
    idBon = models.CharField(
          ("id Bon"), 
          max_length=200,
          blank=False,
          null=False,
          unique=True
    )    
    dateBon = models.DateField()
    store_depart = models.ForeignKey('clientinfo.store', on_delete = models.CASCADE, related_name='bontransfert_mag_dep', blank=True)
    entrepot_depart = models.ForeignKey(Entrepot, on_delete = models.CASCADE, related_name='entdep_transfertmag', blank=True)
    store_arrive = models.ForeignKey('clientinfo.store', on_delete = models.CASCADE, related_name='bontransfert_mag_arr', blank=True)
    entrepot_arrive = models.ForeignKey(Entrepot, on_delete = models.CASCADE, related_name='entarr_transfertmag', blank=True)
    automatiquement = models.BooleanField(blank=True, null=True,default=False)
    valide = models.BooleanField(blank=True, null=True, default=False)
    user = models.ForeignKey(CustomUser,on_delete = models.CASCADE, related_name='mes_bons_transfert_mag', blank=True, null=True, default=None)
    store = models.ForeignKey(store, on_delete=models.CASCADE,blank=True , null=True, default=None)
        
    def __str__(self):
	    return "Bon no: " + str(self.idBon)
	    
class ProduitsEnBonTransfertMag(models.Model):
    BonNo = models.ForeignKey(BonTransfertMagasin, on_delete = models.CASCADE, related_name='produits_en_bon_transfertMag')
    stock_dep = models.ForeignKey(Stock, on_delete = models.CASCADE, related_name='bons_transfertmag_arrive')
    stock_arr = models.ForeignKey(Stock, on_delete = models.CASCADE, related_name='bons_transfertmag_recu')
    quantity = models.IntegerField(default=1)
  
    def __str__(self):
	    return "Bon no: " + str(self.BonNo.idBon) + ",from  Item = " + self.stock_dep.entrepot.name+ ",to   Item = " + self.stock_arr.entrepot.name
	    
class BonRetour(models.Model):
    idBon = models.CharField(
          ("id Bon"), 
          max_length=200,
          blank=False,
          null=False,
          unique=True
    )    
    dateBon = models.DateField()
    totalPrice = models.IntegerField(default=0)
    bonL = models.ForeignKey('ventes.BonSortie', on_delete=models.CASCADE, related_name='MesbonRetours', default=None, null=True, blank=True)
    client =models.ForeignKey('tiers.Client',on_delete = models.CASCADE, related_name='client_bons_retour')
    valide = models.BooleanField(blank=True, null=True, default=False)
    reception_valide = models.BooleanField(blank=True, null=True, default=False)
    store =models.ForeignKey(store,on_delete = models.CASCADE, related_name='store_bons_retour')
    user =models.ForeignKey(CustomUser,on_delete = models.CASCADE, related_name='mes_bons_retour', blank=True, null=True, default=None)        
    def __str__(self):
	    return "Bon no: " + str(self.idBon)

 
class BonEchange(models.Model):
    idBon = models.CharField(
          ("id Bon"), 
          max_length=200,
          blank=False,
          null=False,
          unique=True
    )    
    dateBon = models.DateField()
    totalPrice = models.IntegerField(default=0)
    bonL = models.ForeignKey(BonRetour, on_delete=models.CASCADE, related_name='Mesbonechange', default=None, null=True, blank=True)
    client =models.ForeignKey('tiers.Client',on_delete = models.CASCADE, related_name='client_bons_echange')
    valide = models.BooleanField(blank=True, null=True, default=False)
    store =models.ForeignKey(store,on_delete = models.CASCADE, related_name='store_bons_echange')
    user =models.ForeignKey(CustomUser,on_delete = models.CASCADE, related_name='mes_bons_echange', blank=True, null=True, default=None)
    entrepot = models.ForeignKey('inventory.Entrepot', on_delete = models.CASCADE, related_name='entrepot_bonsechange', default=None, blank=True, null=True)
        
    def __str__(self):
	    return "Bon no: " + str(self.idBon)
 
class BonMaintenance(models.Model):
    idBon = models.CharField(
          ("id Bon"), 
          max_length=200,
          blank=False,
          null=False,
          unique=True
    )    
    dateBon = models.DateField()
    totalPrice = models.IntegerField(default=0)
    bonL = models.ForeignKey(BonRetour, on_delete=models.CASCADE, related_name='Mesbonmaintenance', default=None, null=True, blank=True)
    bonR = models.ForeignKey(BonRetourAncien, on_delete=models.CASCADE, related_name='Mesbonmaintenance', default=None, null=True, blank=True)
    bonLComptoir = models.ForeignKey('comptoire.BonRetourComptoir', on_delete=models.CASCADE, related_name='MesbonmaintenanceComptoir', default=None, null=True, blank=True)
    valide = models.BooleanField(blank=True, null=True, default=False)
    garantie = models.BooleanField(blank=True, null=True, default=False)
    reponse = models.TextField(blank=True, null=True, default="")
    decision = models.TextField(blank=True, null=True, default="")
    store =models.ForeignKey(store,on_delete = models.CASCADE, related_name='store_bons_maintenance')
    user =models.ForeignKey(CustomUser,on_delete = models.CASCADE, related_name='mes_bons_maintenance', blank=True, null=True, default=None)
    entrepot = models.ForeignKey('inventory.Entrepot', on_delete = models.CASCADE, related_name='entrepot_bonsmaintenance', default=None, blank=True, null=True)
    observation = models.TextField(blank=True, null=True, default="")
        
    def __str__(self):
	    return "Bon no: " + str(self.idBon)

class ProduitsEnBonMaintenance(models.Model):
    BonNo = models.ForeignKey(BonMaintenance, on_delete = models.CASCADE, related_name='produits_en_bon_maintenance')
    produit = models.ForeignKey('produits.Product', on_delete = models.CASCADE, related_name='mes_bons_maintenance')
    image1 = models.FileField(upload_to="media/document") 
    image2 = models.FileField(upload_to="media/document") 
    image3 = models.FileField(upload_to="media/document") 
    image4 = models.FileField(upload_to="media/document") 
    quantity = models.IntegerField(default=0) 
    observation = models.TextField(blank=True, null=True, default="")
    

class ProduitsEnBonEchange(models.Model):
    BonNo = models.ForeignKey(BonEchange, on_delete = models.CASCADE, related_name='produits_en_bon_echange')
    stock = models.ForeignKey('produits.Product', on_delete = models.CASCADE, related_name='bons_echange')
    quantity = models.IntegerField(default=1)
    unitprice = models.DecimalField(max_digits=15, decimal_places=2)
    totalprice = models.DecimalField(max_digits=15, decimal_places=2)   
    
    def __str__(self):
	    return "Bon no: " + str(self.BonNo.idBon) + ", Item = " + self.stock.name
 
  
class BonReforme(models.Model):
    idBon = models.CharField(
          ("id Bon"), 
          max_length=200,
          blank=False,
          null=False,
          unique=True
    )    
    dateBon = models.DateField()   
    entrepot = models.ForeignKey(Entrepot,on_delete = models.CASCADE, related_name='entrepot_bons_reforme', blank=True, default=None, null=False) 
    bonretour = models.ForeignKey(BonRetour, on_delete=models.CASCADE, related_name='bonretour_bon_reforme', blank=True, default=None, null=False)
    store =models.ForeignKey(store,on_delete = models.CASCADE, related_name='store_bons_reforme')
    user =models.ForeignKey(CustomUser,on_delete = models.CASCADE, related_name='mes_bons_reforme', blank=True, null=True, default=None)
    def __str__(self):
	    return "Bon no: " + str(self.idBon)

class ProduitsEnBonReforme(models.Model):
    BonNo = models.ForeignKey(BonReforme, on_delete = models.CASCADE, related_name='produits_en_bon_reforme')
    produit = models.ForeignKey('produits.Product', on_delete = models.CASCADE, related_name='mes_bons_reforme')
    quantity = models.IntegerField(default=0) 
    observation = models.TextField(blank=True, null=True, default="")
    def __str__(self):
	    return "Bon no: " + str(self.BonNo.idBon) + ", Item = " + self.produit.name 
 
class BonEntry(models.Model):
    idBon = models.CharField(
          ("id Bon"), 
          max_length=200,
          blank=False,
          null=False,
          unique=True
    )    
    dateBon =models.DateField()
    user =models.ForeignKey(CustomUser,on_delete = models.CASCADE, related_name='mes_bons_entry', blank=True, null=True, default=None)
    fournisseur = models.ForeignKey('tiers.Fournisseur', on_delete = models.CASCADE, related_name='fournisseurs_bons_entry', blank=True , null=True, default=None)
    entrepot = models.ForeignKey(Entrepot, on_delete = models.CASCADE, related_name='Entrepots_bons_entry', blank=True , null=True, default=None)
    store = models.ForeignKey(store, on_delete=models.CASCADE,blank=True , null=True, default=None)
    def __str__(self):
	    return "Bon no: " + str(self.idBon)
 
class BonReintegration(models.Model):
    idBon = models.CharField(
          ("id Bon"), 
          max_length=200,
          blank=False,
          null=False,
          unique=True
    )    
    dateBon =models.DateField()
    user =models.ForeignKey(CustomUser,on_delete = models.CASCADE, related_name='mes_bons_reintegration', blank=True, null=True, default=None)
    bonRetour = models.ForeignKey(BonRetour, on_delete = models.CASCADE, related_name='bonretour_bons_reintegration', blank=True , null=True, default=None)
    entrepot = models.ForeignKey(Entrepot, on_delete = models.CASCADE, related_name='Entrepots_bons_reintegration', blank=True , null=True, default=None)
    store = models.ForeignKey(store, on_delete=models.CASCADE,blank=True , null=True, default=None)   
    def __str__(self):
	    return "Bon no: " + str(self.idBon)

class Bonsortiedestock(models.Model):
    idBon = models.CharField(
          ("id Bon"), 
          max_length=200,
          blank=False,
          null=False,
          unique=True
    )    
    dateBon =models.DateField()
    user = models.ForeignKey(CustomUser,on_delete = models.CASCADE, related_name='mes_bons_sortiesstock',blank=True, null=True, default=None)
    bonL = models.ForeignKey('ventes.BonSortie',on_delete = models.CASCADE, related_name='bonsBl_sortiesstock',blank=True , null=True, default=None)
    entrepot = models.ForeignKey(Entrepot, on_delete = models.CASCADE, related_name='Entrepots_bons_sortiesstock', blank=True , null=True, default=None)
    store = models.ForeignKey(store, on_delete=models.CASCADE,blank=True , null=True, default=None)
    Client =models.ForeignKey(Client, on_delete=models.CASCADE,blank=True , null=True, default=None)
    num_doc = models.CharField(max_length=100, null=True, blank=True, default="")
    Date_doc_Sortie = models.DateField(null=True, blank=True)
    num_constat	= models.CharField(max_length=100, null=True, blank=True, default="")
    Date_constat= models.DateField(null=True, blank=True)
    note = models.TextField( null=True, blank=True, default="")
    
    def __str__(self):
	    return "Bon no: " + str(self.idBon)
 
class BonTransfert(models.Model):
    idBon = models.CharField(
          ("id Bon"), 
          max_length=200,
          blank=False,
          null=False,
          unique=True
    )    
    dateBon = models.DateField()
    entrepot_depart = models.ForeignKey(Entrepot, on_delete = models.CASCADE, related_name='bontransfert_env', blank=True)
    entrepot_arrive = models.ForeignKey(Entrepot, on_delete = models.CASCADE, related_name='bontransfert_rec', blank=True)
    automatiquement = models.BooleanField(blank=True, null=True,default=False)
    valide = models.BooleanField(blank=True, null=True, default=False)
    validation_recu = models.BooleanField(blank=True, null=True, default=True) 
    annule = models.BooleanField(blank=True, null=True, default=False) 
    user = models.ForeignKey(CustomUser,on_delete = models.CASCADE, related_name='mes_bons_transfert', blank=True, null=True, default=None)
    store = models.ForeignKey(store, on_delete=models.CASCADE,blank=True , null=True, default=None)

    def __str__(self):
	    return "Bon no: " + str(self.idBon)
    
class ProduitsEnBonRetour(models.Model):
    BonNo = models.ForeignKey(BonRetour, on_delete = models.CASCADE, related_name='produits_en_bon_retour')
    produit = models.ForeignKey('produits.Product', on_delete = models.CASCADE, related_name='mes_bons_retour')    
    totalprice = models.DecimalField(max_digits=15, decimal_places=2)
    unitprice = models.DecimalField(max_digits=15, decimal_places=2)
    reintegrated = models.BooleanField(default=False)
    image = models.FileField(upload_to="media/document") 
    warranty = models.BooleanField(default=False)
    numseries = models.CharField( 
          max_length=200,
          blank=True,
          null=True,
          default = '',  
    )    
    direction = models.CharField( 
          max_length=50,
          blank=True,
          null=True,
          default = '',  
    )    
    quantity = models.IntegerField(default=1)
  
    def __str__(self):
	    return "Bon no: " + str(self.BonNo.idBon) + ", Item = " + self.produit.name   
   
class ProduitsEnBonTransfert(models.Model):
    BonNo = models.ForeignKey(BonTransfert, on_delete = models.CASCADE, related_name='produits_en_bon_transfert')
    stock_dep = models.ForeignKey(Stock, on_delete = models.CASCADE, related_name='bons_transfert_arrive')
    stock_arr = models.ForeignKey(Stock, on_delete = models.CASCADE, related_name='bons_transfert_recu')
    quantity = models.IntegerField(default=1)
  
    def __str__(self):
	    return "Bon no: " + str(self.BonNo.idBon) + ",from  Item = " + self.stock_dep.entrepot.name+ ",to   Item = " + self.stock_arr.entrepot.name
   
class ProduitsEnBonEntry(models.Model):
    BonNo = models.ForeignKey(BonEntry, on_delete = models.CASCADE, related_name='produits_en_bon_entry')
    stock = models.ForeignKey('produits.Product', on_delete = models.CASCADE, related_name='bons_entry')
    quantity = models.IntegerField(default=1)

    def __str__(self):
	    return "Bon no: " + str(self.BonNo.idBon) + ", Item = " + self.stock.name
 
class ProduitsEnBonReintegration(models.Model):
    BonNo = models.ForeignKey(BonReintegration, on_delete = models.CASCADE, related_name='produits_en_bon_reintegration')
    stock = models.ForeignKey('produits.Product', on_delete = models.CASCADE, related_name='bons_reintegration')
    quantity = models.IntegerField(default=1)

    
    def __str__(self):
	    return "Bon no: " + str(self.BonNo.idBon) + ", Item = " + self.stock.name
 
class ProduitsEnBonSortieStock(models.Model):
    BonNo = models.ForeignKey(Bonsortiedestock, on_delete = models.CASCADE, related_name='produits_en_bon_sortie_stock')
    stock = models.ForeignKey('produits.Product', on_delete = models.CASCADE, related_name='bons_sorties_stock')
    quantity = models.IntegerField(default=1)

    
    def __str__(self):
	    return "Bon no: " + str(self.BonNo.idBon) + ", Item = " + self.stock.name