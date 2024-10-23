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


class CategoryViewset(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class ProductViewset(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class HistoriqueAchatProduitViewset(viewsets.ModelViewSet):
    queryset=HistoriqueAchatProduit.objects.all()
    serializer_class=HistoriqueAchatProduitSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class NumSeriesViewset(viewsets.ModelViewSet):
    queryset=NumSeries.objects.all()
    serializer_class=NumSeriesSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class variantsPrixClientViewset(viewsets.ModelViewSet):
    queryset=variantsPrixClient.objects.all()
    serializer_class=variantsPrixClientSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class PromotionViewset(viewsets.ModelViewSet):
    queryset=Promotion.objects.all()
    serializer_class=PromotionSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class Variantes_productViewset(viewsets.ModelViewSet):
    queryset=Variantes_product.objects.all()
    serializer_class=Variantes_productSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class ProductVariantViewset(viewsets.ModelViewSet):
    queryset=ProductVariant.objects.all()
    serializer_class=ProductVariantSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class historique_prix_achatViewset(viewsets.ModelViewSet):
    queryset=historique_prix_achat.objects.all()
    serializer_class=historique_prix_achatSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class VerificationArchiveViewset(viewsets.ModelViewSet):
    queryset=VerificationArchive.objects.all()
    serializer_class=VerificationArchiveSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class ListProductVerificationArchiveViewset(viewsets.ModelViewSet):
    queryset=ListProductVerificationArchive.objects.all()
    serializer_class=ListProductVerificationArchiveSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]

class codeEAViewset(viewsets.ModelViewSet):
    queryset=codeEA.objects.all()
    serializer_class=codeEASerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
