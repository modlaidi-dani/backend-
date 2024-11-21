from django.urls import path,include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register('store',storeViewset,basename='store')
router.register('jornal',JournalViewset,basename='jornal')
router.register('ploncomptableclass',PlanComptableClassViewset,basename='ploncomptableclass')
router.register('ploncomptableaccount',PlanComptableAccountViewset,basename='ploncomptableaccount')
router.register('compteentreprise',CompteEntrepriseViewset,basename='compteentreprise')
router.register('tax',TaxesViewset,basename='tax')
router.register('valeurdevise',ValeurDeviseViewset,basename='valeurdevise')
router.register('typeclient',typeClientViewset,basename='typeclient')
router.register('devise',DeviseViewset,basename='devise')

urlpatterns = [
    path('',include(router.urls)),
]