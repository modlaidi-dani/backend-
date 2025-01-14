from django.urls import path,include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register('ModeReglement',ModeReglementViewset,basename='ModeReglement')
router.register('depense',depenseViewset,basename='depense')
router.register('equipeEcheanceReglement',EcheanceReglementViewset,basename='equipeEcheanceReglement')
router.register('HistoriqueMontantRecuperer',HistoriqueMontantRecupererViewset,basename='HistoriqueMontantRecuperer')
router.register('Reglement',ReglementViewset,basename='Reglement')
router.register('ReglementFournisseur',ReglementFournisseurViewset,basename='ReglementFournisseur')
router.register('ClotureReglements',ClotureReglementsViewset,basename='ClotureReglements')
router.register('montantCollected',montantCollectedViewset,basename='montantCollected')
router.register('mouvementCaisse',mouvementCaisseViewset,basename='mouvementCaisse')
router.register('TypeDepense',TypeDepenseViewset,basename='TypeDepense')

urlpatterns = [
    path('',include(router.urls)),
]