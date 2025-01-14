from django.urls import path,include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register('Category',CategoryViewset,basename='Category')
router.register('Product',ProductViewset,basename='Product')
router.register('HistoriqueAchatProduit',HistoriqueAchatProduitViewset,basename='HistoriqueAchatProduit')
router.register('NumSeries',NumSeriesViewset,basename='NumSeries')
router.register('variantsPrixClient',variantsPrixClientViewset,basename='variantsPrixClient')
router.register('Promotion',PromotionViewset,basename='Promotion')
router.register('Variantes_product',Variantes_productViewset,basename='Variantes_product')
router.register('ProductVariant',ProductVariantViewset,basename='ProductVariant')
router.register('historique_prix_achat',historique_prix_achatViewset,basename='historique_prix_achat')
router.register('VerificationArchive',VerificationArchiveViewset,basename='VerificationArchive')
router.register('ListProductVerificationArchive',ListProductVerificationArchiveViewset,basename='ListProductVerificationArchive')
router.register('codeEA',codeEAViewset,basename='codeEA')


urlpatterns = [
    path('',include(router.urls)),
]