from django.shortcuts import render

# Create your views here.
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
from rest_framework.filters import SearchFilter
from core.permission import DynamicPermission
from core.filters import  UserFilterBackend, StoreFilter
from core.pagination import PageNumberPagination
from .filters import *
from django_filters.rest_framework import DjangoFilterBackend
class CategoryViewset(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 

class ProductViewset(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[SearchFilter,DjangoFilterBackend, UserFilterBackend,  StoreFilter]
    pagination_class = PageNumberPagination 
    filterset_class=ProduitFiltercategory
    search_fields = ['name', 'reference']
    

class HistoriqueAchatProduitViewset(viewsets.ModelViewSet):
    queryset=HistoriqueAchatProduit.objects.all()
    serializer_class=HistoriqueAchatProduitSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend,  StoreFilter]
    pagination_class = PageNumberPagination 
    

class NumSeriesViewset(viewsets.ModelViewSet):
    queryset=NumSeries.objects.all()
    serializer_class=NumSeriesSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend,  StoreFilter]
    pagination_class = PageNumberPagination 
    

class variantsPrixClientViewset(viewsets.ModelViewSet):
    queryset=variantsPrixClient.objects.all()
    serializer_class=variantsPrixClientSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend,  StoreFilter]
    pagination_class = PageNumberPagination 
    

class PromotionViewset(viewsets.ModelViewSet):
    queryset=Promotion.objects.all()
    serializer_class=PromotionSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend,  StoreFilter]
    pagination_class = PageNumberPagination 
    

class Variantes_productViewset(viewsets.ModelViewSet):
    queryset=Variantes_product.objects.all()
    serializer_class=Variantes_productSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend,  StoreFilter]
    pagination_class = PageNumberPagination 
    

class ProductVariantViewset(viewsets.ModelViewSet):
    queryset=ProductVariant.objects.all()
    serializer_class=ProductVariantSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend,  StoreFilter]
    pagination_class = PageNumberPagination 
    

class historique_prix_achatViewset(viewsets.ModelViewSet):
    queryset=historique_prix_achat.objects.all()
    serializer_class=historique_prix_achatSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend,  StoreFilter]
    pagination_class = PageNumberPagination 
    

class VerificationArchiveViewset(viewsets.ModelViewSet):
    queryset=VerificationArchive.objects.all()
    serializer_class=VerificationArchiveSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend,  StoreFilter]
    pagination_class = PageNumberPagination 
    

class ListProductVerificationArchiveViewset(viewsets.ModelViewSet):
    queryset=ListProductVerificationArchive.objects.all()
    serializer_class=ListProductVerificationArchiveSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend,  StoreFilter]
    pagination_class = PageNumberPagination 
    


class codeEAViewset(viewsets.ModelViewSet):
    queryset=codeEA.objects.all()
    serializer_class=codeEASerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend,  StoreFilter]
    pagination_class = PageNumberPagination 
    

