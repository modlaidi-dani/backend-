from django.urls import path,include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register('MoyenTransport',MoyenTransportViewset,basename='MoyenTransport')
router.register('FicheLivraisonExterne',FicheLivraisonExterneViewset,basename='FicheLivraisonExterne')
router.register('requeteclientinfo',requeteclientinfoViewset,basename='requeteclientinfo')
router.register('CourseLivraison',CourseLivraisonViewset,basename='CourseLivraison')
router.register('BlsEnRequeteClient',BlsEnRequeteClientViewset,basename='BlsEnRequeteClient')
router.register('PreparationStock',PreparationStockViewset,basename='PreparationStock')
router.register('BonTransport',BonTransportViewset,basename='BonTransport')
router.register('ProduitsEnBonTransport',ProduitsEnBonTransportViewset,basename='ProduitsEnBonTransport')
router.register('ReglementTransport',ReglementTransportViewset,basename='ReglementTransport')


urlpatterns = [
    path('',include(router.urls)),
]