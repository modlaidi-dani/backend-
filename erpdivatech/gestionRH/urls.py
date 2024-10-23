from django.urls import path,include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register('RequeteSalarie',RequeteSalarieViewset,basename='RequeteSalarie')
router.register('Event',EventViewset,basename='Event')
router.register('Salarie',SalarieViewset,basename='Salarie')
router.register('ReglementCompte',ReglementCompteViewset,basename='ReglementCompte')
router.register('Conge',CongeViewset,basename='Conge')
router.register('Pointage',PointageViewset,basename='Pointage')
router.register('AvanceSalaire',AvanceSalaireViewset,basename='AvanceSalaire')
router.register('PrixSocial',PrixSocialViewset,basename='PrixSocial')
router.register('HeureSup',HeureSupViewset,basename='HeureSup')
router.register('PrimeMotivation',PrimeMotivationViewset,basename='PrimeMotivation')
router.register('Absence',AbsenceViewset,basename='Absence')
router.register('Contrat',ContratViewset,basename='Contrat')
router.register('Renumeration',RenumerationViewset,basename='Renumeration')
router.register('BoiteArchive',BoiteArchiveViewset,basename='BoiteArchive')


urlpatterns = [
    path('',include(router.urls)),
]