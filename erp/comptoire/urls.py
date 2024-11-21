from django.urls import path,include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register('pointvente',pointVenteViewset,basename='pointvente')
router.register('Emplacement',EmplacementViewset,basename='Emplacement')
router.register('AffectationCaisse',AffectationCaisseViewset,basename='AffectationCaisse')
router.register('Cloture',ClotureViewset,basename='Cloture')
router.register('BonComptoire',BonComptoireViewset,basename='BonComptoire')
router.register('BonRectification',BonRectificationViewset,basename='BonRectification')
router.register('verssement',verssementViewset,basename='verssement')
router.register('BonRetourComptoir',BonRetourComptoirViewset,basename='BonRetourComptoir')
router.register('ProduitsEnBonRetourComptoir',ProduitsEnBonRetourComptoirViewset,basename='ProduitsEnBonRetourComptoir')
router.register('ProduitsEnBonComptoir',ProduitsEnBonComptoirViewset,basename='ProduitsEnBonComptoir')
router.register('ProduitsEnBonRectif',ProduitsEnBonRectifViewset,basename='ProduitsEnBonRectif')

urlpatterns = [
    path('',include(router.urls)),
]