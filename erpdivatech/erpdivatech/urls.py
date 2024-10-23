from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('clientinfo/', include('clientinfo.urls')),
    path('achats/', include('achats.urls')),
    path('comptoire/', include('comptoire.urls')),
    path('gestionRH/', include('gestionRH.urls')),
    path('inventory/', include('inventory.urls')),
    path('logistique/', include('logistique.urls')),
    path('produits/', include('produits.urls')),
    path('tiers/', include('tiers.urls')),
    path('user/', include('user.urls')),
    path('ventes/', include('ventes.urls')),
    path('reglements/', include('reglements.urls')),    
]