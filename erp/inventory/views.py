from django.shortcuts import render
from .models import * 
from .serializers import * 
# from permissions import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser
from rest_framework import response,status
from rest_framework_simplejwt.authentication import JWTAuthentication
# from permissions import IsManager
from core.permission import DynamicPermission
from core.filters import  UserFilterBackend, StoreFilter
from core.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import *
class EntrepotViewset(viewsets.ModelViewSet):
    queryset=Entrepot.objects.all()
    serializer_class=EntrepotSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    def create(self, request):
        store = request.session["store"] 
        request.data["store"] = store  
        return super().create(request) 


    
class InventaireAnnuelViewset(viewsets.ModelViewSet):
    queryset=InventaireAnnuel.objects.all()
    serializer_class=InventaireAnnuelSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class equipeInventaireViewset(viewsets.ModelViewSet):
    queryset=equipeInventaire.objects.all()
    serializer_class=equipeInventaireSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class BonRetourAncienViewset(viewsets.ModelViewSet):
    queryset=BonRetourAncien.objects.all()
    serializer_class=BonRetourAncienSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class ProduitsEnBonRetourAncienViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnBonRetourAncien.objects.all()
    serializer_class=ProduitsEnBonRetourAncienSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class produitEnInventaireAnnuelViewset(viewsets.ModelViewSet):
    queryset=produitEnInventaireAnnuel.objects.all()
    serializer_class=produitEnInventaireAnnuelSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class StockViewset(viewsets.ModelViewSet):
    queryset=Stock.objects.all()
    serializer_class=StockSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission]
    filter_backends=[ SearchFilter,DjangoFilterBackend, UserFilterBackend, StoreFilter]
    filterset_class=StockFilter
    pagination_class = PageNumberPagination 
    search_fields = ['product__name', 'product__reference']
    
    

class BonTransfertMagasinViewset(viewsets.ModelViewSet):
    queryset=BonTransfertMagasin.objects.all()
    serializer_class=BonTransfertMagasinSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class ProduitsEnBonTransfertMagViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnBonTransfertMag.objects.all()
    serializer_class=ProduitsEnBonTransfertMagSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class BonRetourViewset(viewsets.ModelViewSet):
    queryset=BonRetour.objects.all()
    serializer_class=BonRetourSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission]
    filter_backends=[ SearchFilter,DjangoFilterBackend, UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination
    filterset_class=BonRetourFilter
    search_fields = ['idBon','bonL__idBon','client__name', 'produits_en_bon_retour__produit__reference','produits_en_bon_retour__produit__name']
    

class BonEchangeViewset(viewsets.ModelViewSet):
    queryset=BonEchange.objects.all()
    serializer_class=BonEchangeSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class BonMaintenanceViewset(viewsets.ModelViewSet):
    queryset=BonMaintenance.objects.all()
    serializer_class=BonMaintenanceSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class ProduitsEnBonMaintenanceViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnBonMaintenance.objects.all()
    serializer_class=ProduitsEnBonMaintenanceSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class ProduitsEnBonEchangeViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnBonEchange.objects.all()
    serializer_class=ProduitsEnBonEchangeSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class BonReformeViewset(viewsets.ModelViewSet):
    queryset=BonReforme.objects.all()
    serializer_class=BonReformeSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class ProduitsEnBonReformeViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnBonReforme.objects.all()
    serializer_class=ProduitsEnBonReformeSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class BonEntryViewset(viewsets.ModelViewSet):
    queryset=BonEntry.objects.all()
    serializer_class=BonEntrySerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission]
    filter_backends=[ SearchFilter,DjangoFilterBackend, UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination
    filterset_class=BonentyFilter
    search_fields = ['idBon','fournisseur__acronym', 'produits_en_bon_entry__stock__reference','produits_en_bon_entry__stock__name']
     
    

class BonReintegrationViewset(viewsets.ModelViewSet):
    queryset=BonReintegration.objects.all()
    serializer_class=BonReintegrationSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class BonsortiedestockViewset(viewsets.ModelViewSet):
    queryset=Bonsortiedestock.objects.all()
    serializer_class=BonsortiedestockSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class BonTransfertViewset(viewsets.ModelViewSet):
    queryset=BonTransfert.objects.all()
    serializer_class=BonTransfertSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class ProduitsEnBonRetourViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnBonRetour.objects.all()
    serializer_class=ProduitsEnBonRetourSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class ProduitsEnBonTransfertViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnBonTransfert.objects.all()
    serializer_class=ProduitsEnBonTransfertSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class ProduitsEnBonEntryViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnBonEntry.objects.all()
    serializer_class=ProduitsEnBonEntrySerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class ProduitsEnBonReintegrationViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnBonReintegration.objects.all()
    serializer_class=ProduitsEnBonReintegrationSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class ProduitsEnBonSortieStockViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnBonSortieStock.objects.all()
    serializer_class=ProduitsEnBonSortieStockSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    


