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
from core.permission import DynamicPermission
from core.filters import UserFilterBackend


class CategoryViewset(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated,DynamicPermission]
    filterset_class=[UserFilterBackend]

class ProductViewset(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated,DynamicPermission]
    filterset_class=[UserFilterBackend]

class HistoriqueAchatProduitViewset(viewsets.ModelViewSet):
    queryset=HistoriqueAchatProduit.objects.all()
    serializer_class=HistoriqueAchatProduitSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated,DynamicPermission]
    filterset_class=[UserFilterBackend]

class NumSeriesViewset(viewsets.ModelViewSet):
    queryset=NumSeries.objects.all()
    serializer_class=NumSeriesSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated,DynamicPermission]
    filterset_class=[UserFilterBackend]

class variantsPrixClientViewset(viewsets.ModelViewSet):
    queryset=variantsPrixClient.objects.all()
    serializer_class=variantsPrixClientSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated,DynamicPermission]
    filterset_class=[UserFilterBackend]

class PromotionViewset(viewsets.ModelViewSet):
    queryset=Promotion.objects.all()
    serializer_class=PromotionSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated,DynamicPermission]
    filterset_class=[UserFilterBackend]

class Variantes_productViewset(viewsets.ModelViewSet):
    queryset=Variantes_product.objects.all()
    serializer_class=Variantes_productSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated,DynamicPermission]
    filterset_class=[UserFilterBackend]

class ProductVariantViewset(viewsets.ModelViewSet):
    queryset=ProductVariant.objects.all()
    serializer_class=ProductVariantSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated,DynamicPermission]
    filterset_class=[UserFilterBackend]

class historique_prix_achatViewset(viewsets.ModelViewSet):
    queryset=historique_prix_achat.objects.all()
    serializer_class=historique_prix_achatSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated,DynamicPermission]
    filterset_class=[UserFilterBackend]

class VerificationArchiveViewset(viewsets.ModelViewSet):
    queryset=VerificationArchive.objects.all()
    serializer_class=VerificationArchiveSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated,DynamicPermission]
    filterset_class=[UserFilterBackend]

class ListProductVerificationArchiveViewset(viewsets.ModelViewSet):
    queryset=ListProductVerificationArchive.objects.all()
    serializer_class=ListProductVerificationArchiveSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated,DynamicPermission]
    filterset_class=[UserFilterBackend]


class codeEAViewset(viewsets.ModelViewSet):
    queryset=codeEA.objects.all()
    serializer_class=codeEASerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated,DynamicPermission]
    filterset_class=[UserFilterBackend]

