from django.urls import path,include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register('boncommande',BonCommandeAchatViewset,basename='boncommande')
router.register('produitenbc',ProduitsEnBonCommandesAchatViewset,basename='produitenbc')
router.register('dossierachat',DossierAchatViewset,basename='dossierachat')
router.register('bonachat',BonAchatViewset,basename='bonachat')
router.register('facturachat',FactureAchatViewset,basename='facturachat')
router.register('produitenfactureachat',ProduitsEnFactureAchatViewset,basename='produitenfactureachat')
router.register('produitenbonachat',ProduitsEnBonAchatViewset,basename='produitenbonachat')
router.register('avoirachat',AvoirAchatViewset,basename='avoirachat')
router.register('bonreciption',BonReceptionViewset,basename='bonreciption')
router.register('produitenBR',ProduitsEnBonReceptionViewset,basename='produitenBR')
router.register('projetcredit',ProjetCreditViewset,basename='projetcredit')
router.register('creditnote',CreditNoteViewset,basename='creditnote')
router.register('produitsencredit',ProduitsEnCreditNoteViewset,basename='produitsencredit')

urlpatterns = [
    path('',include(router.urls)),
]