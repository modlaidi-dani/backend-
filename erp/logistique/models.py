from django.db import models
from datetime import datetime
# Create your models here.

class MoyenTransport(models.Model):
    immatriculation = models.CharField(max_length=255, null=True, blank=True, default='')
    designation = models.CharField(max_length=255, null=True, blank=True, default='')
    date = models.DateField(null=True, blank=True,)
    store = models.ForeignKey('clientinfo.store', related_name = "store_moyenstransport", on_delete=models.CASCADE, null=True, blank=True, default=None)

class FicheLivraisonExterne(models.Model):
    client = models.CharField(max_length=255, null=True, blank=True, default='')
    adresse = models.CharField(max_length=255, null=True, blank=True, default='')
    date = models.DateField(null=True, blank=True)  
    transporteur = models.CharField(max_length=255, null=True, blank=True, default='')
    modePaiement = models.CharField(max_length=255, null=True, blank=True, default='')
    montant = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    numeroColis = models.IntegerField(default=1)
    note = models.CharField(max_length=255, null=True, blank=True, default='')
    
class requeteclientinfo(models.Model):
    client = models.ForeignKey('tiers.Client', on_delete = models.CASCADE, related_name='clients_requetes', blank=True , null=True, default=None)  
    dateReq = models.DateField(null=True, blank=True)  
    etat = models.CharField(max_length=255, null=True, blank=True, default='')
    modePaiement = models.CharField(max_length=255, null=True, blank=True, default='')
    note = models.CharField(max_length=255, null=True, blank=True, default='')

class CourseLivraison(models.Model):
    chauffeur =models.ForeignKey('user.CustomUser', on_delete = models.CASCADE, related_name='mes_courses', blank=True , null=True, default=None)
    adresse = models.CharField(max_length=255, null=True, blank=True, default='')
    note = models.CharField(max_length=255, null=True, blank=True, default='')
    dateTimeAffectation = models.DateTimeField(null=True, blank=True)  
    dateTimeDebut = models.DateTimeField(null=True, blank=True)  
    dateTimeFin = models.DateTimeField(null=True, blank=True)    
    moyen_transport = models.ForeignKey(MoyenTransport, on_delete=models.CASCADE, related_name='courses', blank=False, null=False)
    typeCourse = models.CharField(max_length=255, null=True, blank=True, default='') #livraison courier / transporteur
    transporteur = models.CharField(max_length=255, null=True, blank=True, default='')
    bonlivraison = models.ForeignKey('ventes.BonSortie', related_name = "bonL_course", on_delete=models.CASCADE, blank=False, null=False)
    montant = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default =0)
    fraisTransport = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default =0)
    montantrecupere = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default =0)
    tempsCourse = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    etat = models.CharField(max_length=255, null=True, blank=True, default='')
    
class BlsEnRequeteClient(models.Model):
    requete = models.ForeignKey(requeteclientinfo, related_name = "bonsL_enreq", on_delete=models.CASCADE, blank=False, null=False)
    bonlivraison = models.ForeignKey('ventes.BonSortie', related_name = "bonsL_requests", on_delete=models.CASCADE, blank=False, null=False)
    modePaiement = models.CharField(max_length=255, null=True, blank=True, default='')
    etat_livraison =  models.CharField(max_length=255, null=True, blank=True, default='')
    note = models.CharField(max_length=255, null=True, blank=True, default='')   
    
class PreparationStock(models.Model):
    idBon = models.CharField(max_length=255, null=True, blank=True, default='')
    bonEntry = models.ForeignKey('inventory.BonEntry', related_name = "bonsE_preparation", on_delete=models.CASCADE, blank=False, null=False)
    datePrep = models.DateTimeField()    
    
class BonTransport(models.Model):
    idBon = models.CharField(max_length=255, null=True, blank=True, default='')
    bonlivraison = models.ForeignKey('ventes.BonSortie', related_name = "bonsL_transports", on_delete=models.CASCADE, blank=False, null=False)
    moyen_transport = models.ForeignKey(MoyenTransport, on_delete=models.CASCADE, blank=False, null=False)
    chauffeur = models.CharField(max_length=255, null=True, blank=True, default='')
    date_depart = models.DateTimeField()
    adresse_livraison = models.CharField(max_length=255, null=True, blank=True, default='')
    client = models.ForeignKey('tiers.Client', on_delete = models.CASCADE, related_name='clients_bonstransport', blank=True , null=True, default=None)
    frais_Livraison = models.CharField(max_length=255, null=True, blank= True, default='')
    store = models.ForeignKey('clientinfo.store', related_name = "store_bontransport", on_delete=models.CASCADE, null=True, blank=True, default=None)
    user =models.ForeignKey('user.CustomUser', on_delete = models.CASCADE, related_name='mes_bonstransport', blank=True , null=True, default=None)
    etat_livraison =  models.CharField(max_length=255, null=True, blank=True, default='')
class ProduitsEnBonTransport(models.Model):
    BonNo = models.ForeignKey(BonTransport, on_delete = models.CASCADE, related_name='produits_en_bon_transport')
    produit = models.ForeignKey('produits.Product', on_delete = models.CASCADE, related_name='mes_bons_transport')    
    quantity = models.IntegerField(default=1)
    livre = models.BooleanField(default=False)
  
    def __str__(self):
	    return "Bon no: " + str(self.BonNo.idBon) + ", Item = " + self.produit.name  
            
class ReglementTransport(models.Model):
    montant = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date = models.DateField()
    bon_transport = models.ForeignKey(BonTransport, on_delete = models.CASCADE, related_name='reglements_bontransport')
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, default=None, null=True, blank=True)
    store = models.ForeignKey('clientinfo.store', on_delete=models.CASCADE, default=None, null=True, blank=True)