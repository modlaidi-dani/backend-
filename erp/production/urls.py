from django.urls import path,include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register('ordreFabrication',ordreFabricationViewset,basename='ordreFabrication')
router.register('ProduitsEnOrdreFabrication',ProduitsEnOrdreFabricationViewset,basename='ProduitsEnOrdreFabrication')
router.register('ProduitProductionBL',ProduitProductionBLViewset,basename='ProduitProductionBL')
router.register('ProduitProductionFac',ProduitProductionFacViewset,basename='ProduitProductionFac')



urlpatterns = [
    path('',include(router.urls)),
    ]