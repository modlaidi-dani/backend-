from django.urls import path,include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register('Banque',BanqueViewset,basename='Banque')
router.register('Agence',AgenceViewset,basename='Agence')
router.register('Fournisseur',FournisseurViewset,basename='Fournisseur')
router.register('Region',RegionViewset,basename='Region')
router.register('Client',ClientViewset,basename='Client')
router.register('ProspectionClient',ProspectionClientViewset,basename='ProspectionClient')
router.register('CompteBancaire',CompteBancaireViewset,basename='CompteBancaire')
router.register('Tentatives',TentativesViewset,basename='Tentatives')


urlpatterns = [
    path('',include(router.urls)),
]