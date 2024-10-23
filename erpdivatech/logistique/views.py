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


class MoyenTransportViewset(viewsets.ModelViewSet):
    queryset=MoyenTransport.objects.all()
    serializer_class=MoyenTransportSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class FicheLivraisonExterneViewset(viewsets.ModelViewSet):
    queryset=FicheLivraisonExterne.objects.all()
    serializer_class=FicheLivraisonExterneSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class requeteclientinfoViewset(viewsets.ModelViewSet):
    queryset=requeteclientinfo.objects.all()
    serializer_class=requeteclientinfoSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class CourseLivraisonViewset(viewsets.ModelViewSet):
    queryset=CourseLivraison.objects.all()
    serializer_class=CourseLivraisonSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class BlsEnRequeteClientViewset(viewsets.ModelViewSet):
    queryset=BlsEnRequeteClient.objects.all()
    serializer_class=BlsEnRequeteClientSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class PreparationStockViewset(viewsets.ModelViewSet):
    queryset=PreparationStock.objects.all()
    serializer_class=PreparationStockSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class BonTransportViewset(viewsets.ModelViewSet):
    queryset=BonTransport.objects.all()
    serializer_class=BonTransportSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class ProduitsEnBonTransportViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnBonTransport.objects.all()
    serializer_class=ProduitsEnBonTransportSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class ReglementTransportViewset(viewsets.ModelViewSet):
    queryset=ReglementTransport.objects.all()
    serializer_class=ReglementTransportSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
