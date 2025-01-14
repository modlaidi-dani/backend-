from django.urls import path,include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register('ArchivageBonSortie',ArchivageBonSortieViewset,basename='ArchivageBonSortie')
router.register('ArchivageProduitsEnBonSortie',ArchivageProduitsEnBonSortieViewset,basename='ArchivageProduitsEnBonSortie')
router.register('ArchivageFacture',ArchivageFactureViewset,basename='ArchivageFacture')
router.register('ArchivageProduitsEnFacture',ArchivageProduitsEnFactureViewset,basename='ArchivageProduitsEnFacture')

urlpatterns = [
    path('',include(router.urls)),
]