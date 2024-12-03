from django.db import models

from ventes.models import ProduitsEnBonSortie,ProduitsEnFacture


class ordreFabrication(models.Model):
    entrepot_destocker =  models.ForeignKey('inventory.Entrepot', on_delete=models.CASCADE, related_name='ordre_fabrication_destock', null=True, blank=True)
    entrepot_stocker =  models.ForeignKey('inventory.Entrepot', on_delete=models.CASCADE, related_name='ordre_fabrication_stock', null=True, blank=True)
    pc_created = models.ForeignKey('produits.Product', on_delete = models.CASCADE, related_name='ordre_creation')
    store = models.ForeignKey('clientInfo.store', on_delete=models.CASCADE, null=True, blank=True)
    codeOrdre = models.CharField(max_length=255)

class ProduitsEnOrdreFabrication(models.Model):
    BonNo = models.ForeignKey(ordreFabrication, on_delete = models.CASCADE, related_name='produits_en_ordre_fabrication')
    stock = models.ForeignKey('produits.Product', on_delete = models.CASCADE, related_name='ordres_fabriquation')
    quantity = models.IntegerField(default=1)


class ProduitProductionBL(models.Model):
    ProdenBL=models.ForeignKey(ProduitsEnBonSortie, on_delete = models.CASCADE, related_name='produits_en_PEnOrdre',null=True)
    ProdPid = models.ForeignKey(ProduitsEnOrdreFabrication, on_delete = models.CASCADE, related_name='produits_en_bl')
    quantity = models.IntegerField(default=1)

class ProduitProductionFac(models.Model):
    ProdenFa=models.ForeignKey(ProduitsEnFacture, on_delete = models.CASCADE, related_name='produits_en_Ordre',null=True)
    ProdPid = models.ForeignKey(ProduitsEnOrdreFabrication, on_delete = models.CASCADE, related_name='produits_en_fac')
    quantity = models.IntegerField(default=1)