from django.urls import path,include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register('costumeruser',CustomUserViewset,basename='costumeruser')
router.register('costumergroupe',CustomGroupViewset,basename='costumergroupe')
router.register('equipe',EquipeViewset,basename='equipe')
router.register('permission',UserCustomPermissionViewset,basename='permission')
router.register('cordinates',cordinatesViewset,basename='cordinates')

urlpatterns = [
    path('',include(router.urls)),
    path('UserActuel', UserActuel.as_view(), name='UserActuel'),
]