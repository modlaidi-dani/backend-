from django.urls import path,include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register('ProduitsEnBonCommande',ProduitsEnBonCommandeViewset,basename='ProduitsEnBonCommande')
router.register('Facture',FactureViewset,basename='Facture')
router.register('AvoirVente',AvoirVenteViewset,basename='AvoirVente')
router.register('validationBl',validationBlViewset,basename='validationBl')
router.register('BonSortie',BonSortieViewset,basename='BonSortie')
router.register('DemandeTransfert',DemandeTransfertViewset,basename='DemandeTransfert')
router.register('ConfirmationBl',ConfirmationBlViewset,basename='ConfirmationBl')
router.register('ProduitsEnBonSortie',ProduitsEnBonSortieViewset,basename='ProduitsEnBonSortie')
router.register('BonGarantie',BonGarantieViewset,basename='BonGarantie')
router.register('ProduitsEnBonGarantie',ProduitsEnBonGarantieViewset,basename='ProduitsEnBonGarantie')
router.register('BonDevis',BonDevisViewset,basename='BonDevis')
router.register('ProduitsEnBonDevis',ProduitsEnBonDevisViewset,basename='ProduitsEnBonDevis')
router.register('BonCommande',BonCommandeViewset,basename='BonCommande')
router.register('ProduitsEnFacture',ProduitsEnFactureViewset,basename='ProduitsEnFacture')


urlpatterns = [
    path('',include(router.urls)),
]