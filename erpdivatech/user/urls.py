from django.urls import path,include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register('costumeruser',CustomUserViewset,basename='costumeruser')
router.register('costumergroupe',CustomGroupViewset,basename='costumergroupe')
router.register('equipe',EquipeViewset,basename='equipe')

urlpatterns = [
    path('',include(router.urls)),
]