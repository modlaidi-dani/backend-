from django.db import models
from clientinfo.models import store, typeClient
from user.models import CustomUser
from django.contrib.auth.models import Permission
from datetime import datetime, timedelta
from inventory.models import ProduitsEnBonEntry, ProduitsEnBonRetour
# from ventes.models import ProduitsEnBonSortie
# from comptoire.models import ProduitsEnBonComptoir
# class ProduitsCustomPermission(Permission):
#     class Meta:
#         verbose_name = 'Custom Permission'
#         verbose_name_plural = 'Custom Permissions'
       
class Category(models.Model):
     MotherCategory = models.ForeignKey('self', on_delete=models.SET_NULL, default=None, null=True, blank=True, related_name='variants')
     kit = models.BooleanField(default=True)
     kitcomponents = models.TextField(default='')
     Libellé = models.CharField(max_length=100)
     categoryDesc = models.CharField(max_length=250, default="", blank=True, null=True)
     status = models.BooleanField(default=True)
     pc_component = models.CharField(max_length=250, default="", blank=True, null=True)
     store=models.ForeignKey(store, on_delete=models.CASCADE, default=None, null=True, blank=True)
     
     def __str__(self) :
         return f'{self.Libellé}'
         

               
class Product(models.Model):
    reference = models.CharField( ("Référence du produit"), help_text=("Référence interne pour ce produit"),
          max_length=120,
          blank=False,
          null=False,
          unique=False
    )
    parent_product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name="myvariants",default=None, null=True, blank=True)
    name = models.CharField( ("Désignation"), help_text=("La désignation du produit"),
        max_length=200,
        blank=False,
        null=True
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", blank=True, null=True)
    prix_vente = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    prix_vente_pc = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    prix_vente_kit = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    prix_achat = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    prix_livraison = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    tva = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    tva_douan = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    marge = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    initial_qte = models.IntegerField()
    QuantityPerCarton = models.IntegerField(default=0)
    TotalQte = models.IntegerField(default=0)
    reforme = models.BooleanField(default=False)
    fournisseur = models.CharField(max_length=100, default='', blank=True)
    store = models.ForeignKey(store, on_delete=models.CASCADE, default=None, null=True, blank=True)
    
  
    def __str__(self):
	    return f"Name: {self.name}, ID: {self.id}"

class HistoriqueAchatProduit(models.Model):
    produit =  models.ForeignKey(Product, on_delete=models.CASCADE, related_name='monHIstoriqueAchat',  default=None, null=True, blank=True) 
    qty_qctuelle = models.IntegerField(default= 0)
    prix_achat_actuelle = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    qty_achete = models.IntegerField(default= 0)
    prix_achat= models.DecimalField(max_digits=15, decimal_places=2, default=0)
    prix_achat_calcule = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    dateAchat = models.DateField()
    
class codeEA(models.Model):
    produit =  models.ForeignKey(Product, on_delete=models.CASCADE, related_name='moncodeEAN',  default=None, null=True, blank=True)
    code = models.CharField(max_length=250)

    
class NumSeries(models.Model):
    produit =  models.ForeignKey(Product, on_delete=models.CASCADE, related_name='myserialnumbers',  default=None, null=True, blank=True)
    numseries = models.CharField(max_length=250)
    used = models.BooleanField(default=False)
  
   
class variantsPrixClient(models.Model):
     type_client = models.ForeignKey('clientinfo.typeClient', on_delete=models.CASCADE, related_name="prix_var",default='', blank=True)
     produit =  models.ForeignKey(Product, on_delete=models.CASCADE, related_name="produit_var",default='', blank=True)
     prix_vente = models.DecimalField(max_digits=15, decimal_places=2, default=0)
     prix_vente_pc = models.DecimalField(max_digits=15, decimal_places=2, default=0)
     prix_vente_kit = models.DecimalField(max_digits=15, decimal_places=2, default=0)
     prix_vente_carton = models.DecimalField(max_digits=15, decimal_places=2, default=0)
     
class Promotion(models.Model):
    type_client = models.ForeignKey('clientinfo.TypeClient', on_delete=models.CASCADE,
                                    related_name="promotions", default='', blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="promotions",
                                default='', blank=True)
    prix_vente = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    prix_vente_pc = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    prix_vente_kit = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    prix_vente_carton = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    
class Variantes_product(models.Model):
    variant_lib = models.CharField(max_length=100)
    values_list = models.CharField(max_length=25)
    def __str__(self):
	    return f'{self.variant_lib} : {self.values_list}' 
    
class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variant_set')
    variant = models.ForeignKey(Variantes_product, on_delete=models.CASCADE, related_name='variant_set', default=None, null=True, blank=True)
    value = models.CharField(max_length=10)
    quantity = models.PositiveIntegerField(default=0)
    reference = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
	    return f'{self.product} : {self.variant}' 
    
class historique_prix_achat(models.Model):
     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products",default='', blank=True)
     version = models.IntegerField()
     prix_achat_original = models.DecimalField(max_digits=15, decimal_places=2, default=0)
     prix_achat_newer = models.DecimalField(max_digits=15, decimal_places=2, default=0)
  
class VerificationArchive(models.Model):
    codeArchive = models.CharField(max_length=255)
    store = models.ForeignKey(store, on_delete=models.CASCADE, null=True, blank=True)
    entrepot = models.ForeignKey('inventory.Entrepot', on_delete=models.CASCADE, null=True, blank=True)
    date_verification = models.DateTimeField(auto_now_add=True)
    def get_produit(self):
         return self.produits_verification.all()
      
class ListProductVerificationArchive(models.Model):
    verification = models.ForeignKey(VerificationArchive, on_delete=models.CASCADE, related_name="produits_verification")
    product_reference = models.CharField(max_length=255)
    realQuantity = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    verification_result = models.CharField(max_length=255)