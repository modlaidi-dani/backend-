from django.urls import path,include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register('Entrepot',EntrepotViewset,basename='Entrepot')
router.register('InventaireAnnuel',InventaireAnnuelViewset,basename='InventaireAnnuel')
router.register('equipeInventaire',equipeInventaireViewset,basename='equipeInventaire')
router.register('BonRetourAncien',BonRetourAncienViewset,basename='BonRetourAncien')
router.register('ProduitsEnBonRetourAncien',ProduitsEnBonRetourAncienViewset,basename='ProduitsEnBonRetourAncien')
router.register('produitEnInventaireAnnuel',produitEnInventaireAnnuelViewset,basename='produitEnInventaireAnnuel')
router.register('Stock',StockViewset,basename='Stock')
router.register('BonTransfertMagasin',BonTransfertMagasinViewset,basename='BonTransfertMagasin')
router.register('ProduitsEnBonTransfertMag',ProduitsEnBonTransfertMagViewset,basename='ProduitsEnBonTransfertMag')
router.register('BonRetour',BonRetourViewset,basename='BonRetour')
router.register('BonEchange',BonEchangeViewset,basename='BonEchange')
router.register('BonMaintenance',BonMaintenanceViewset,basename='BonMaintenance')
router.register('ProduitsEnBonMaintenance',ProduitsEnBonMaintenanceViewset,basename='ProduitsEnBonMaintenance')
router.register('ProduitsEnBonEchange',ProduitsEnBonEchangeViewset,basename='ProduitsEnBonEchange')
router.register('BonReforme',BonReformeViewset,basename='BonReforme')
router.register('ProduitsEnBonReforme',ProduitsEnBonReformeViewset,basename='ProduitsEnBonReforme')
router.register('BonEntry',BonEntryViewset,basename='BonEntry')
router.register('BonReintegration',BonReintegrationViewset,basename='BonReintegration')
router.register('Bonsortiedestock',BonsortiedestockViewset,basename='Bonsortiedestock')
router.register('BonTransfert',BonTransfertViewset,basename='BonTransfert')
router.register('ProduitsEnBonRetour',ProduitsEnBonRetourViewset,basename='ProduitsEnBonRetour')
router.register('ProduitsEnBonTransfert',ProduitsEnBonTransfertViewset,basename='ProduitsEnBonTransfert')
router.register('ProduitsEnBonEntry',ProduitsEnBonEntryViewset,basename='ProduitsEnBonEntry')
router.register('ProduitsEnBonReintegration',ProduitsEnBonReintegrationViewset,basename='ProduitsEnBonReintegration')
router.register('ProduitsEnBonSortieStock',ProduitsEnBonSortieStockViewset,basename='ProduitsEnBonSortieStock')


urlpatterns = [
    path('',include(router.urls)),
]