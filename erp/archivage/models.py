from django.db import models
from ventes.models import *
# Create your models here.
class ArchivageBonSortie(models.Model):
    bon_sortie = models.ForeignKey(BonSortie, on_delete=models.CASCADE,related_name='bon_sortie_archive')
    Reglement_etat_CHOICES = [
        ("non-regle", "non-regle"),
        ("regle", "regle"),     
    ]
    idBon = models.CharField(
          ("id Bon"), 
          max_length=200,
           
          null=False,
          unique=False
    )   
    user_update= models.ForeignKey('user.CustomUser',on_delete = models.CASCADE)
    date_update=models.DateField()
    dateBon =models.DateField()
    client =models.ForeignKey('tiers.Client',on_delete = models.CASCADE)
    totalPrice = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    user =models.ForeignKey('user.CustomUser',on_delete = models.CASCADE,  blank=True,related_name="archive_bonsortie")
    entrepot = models.ForeignKey('inventory.Entrepot', on_delete=models.CASCADE, default=None, blank=True, null=True)
    mode_reglement = models.ForeignKey('reglements.ModeReglement', on_delete = models.CASCADE,  null=True, blank=True, default=None)
    echeance_reglement = models.ForeignKey('reglements.EcheanceReglement', on_delete = models.CASCADE,  null=True, blank=True, default=None)
    banque_Reglement = models.ForeignKey('tiers.Banque', on_delete=models.CASCADE, blank=True, null=True, default=None )
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
    store = models.ForeignKey('clientInfo.store', on_delete = models.CASCADE,  null=True, blank=True, default=None)
class ArchivageProduitsEnBonSortie(models.Model):
    produitsenbs = models.ForeignKey(ProduitsEnBonSortie, on_delete=models.CASCADE,related_name='produit_archivage')
    bon_archiv=models.ForeignKey(ArchivageBonSortie, on_delete=models.CASCADE,related_name='produits_archivageBL')
    BonNo = models.ForeignKey(BonSortie, on_delete = models.CASCADE)
    stock = models.ForeignKey('produits.Product', on_delete = models.CASCADE)
    kit = models.TextField(default="")
    quantity = models.IntegerField(default=1)
    unitprice = models.DecimalField(max_digits=15, decimal_places=2)
    totalprice = models.DecimalField(max_digits=15, decimal_places=2)   
    entrepot = models.ForeignKey('inventory.Entrepot', on_delete = models.CASCADE, default=None, blank=True, null=True)
    def __str__(self):
	    return "Bon no: " + str(self.BonNo.idBon) + ", Item = " + self.stock.name

# class ArchivageFacture(models.Model):
#     Reglement_etat_CHOICES = [
#         ("en Attente", "en Attente"),
#         ("Règlement Reçu", "Règlement Reçu"),
#         ("Expédié", "Expédié"),
#         ("Facture", "Facture"),
#         ("Facture Comptabilisé", "Facture Comptabilisé"),
#     ]
#     facture=models.ForeignKey(Facture, on_delete = models.CASCADE)
#     user_update= models.ForeignKey('user.CustomUser',on_delete = models.CASCADE)
#     date_update=models.DateField()
#     codeFacture = models.CharField( max_length=200, null=False,unique=True)  
#     date_facture = models.DateField()
#     date_reglement = models.DateField(default=datetime.now)
#     client = models.ForeignKey('tiers.Client', on_delete = models.CASCADE)
#     store = models.ForeignKey('clientInfo.store', on_delete=models.CASCADE, null=True, blank=True, default=None)
#     BonS = models.ForeignKey(BonSortie, on_delete = models.CASCADE, default=None, blank=True, null=True)
#     mode_reglement = models.ForeignKey('reglements.ModeReglement', on_delete = models.CASCADE,  null=True, blank=True, default=None)
#     echeance_reglement = models.ForeignKey('reglements.EcheanceReglement', on_delete = models.CASCADE,  null=True, blank=True, default=None)
#     banque_Reglement = models.ForeignKey('tiers.Banque', on_delete=models.CASCADE,  blank=True, null=True, default=None )
#     num_cheque_reglement = models.CharField(max_length=2500 , default="", null=True, blank =True)
#     Remise = models.CharField(max_length=20,null=True, blank=True, default='')
#     etat_reglement = models.CharField( max_length=30, choices=Reglement_etat_CHOICES) 
#     shippingCost = models.DecimalField(max_digits=15, decimal_places=2 , null=True, blank=True)
#     totalPrice = models.IntegerField(default=0)
#     valide = models.BooleanField(default=False)
#     ferme =  models.BooleanField(default=False)
#     regle = models.BooleanField(default=False)