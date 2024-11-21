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


class BanqueViewset(viewsets.ModelViewSet):
    queryset=Banque.objects.all()
    serializer_class=BanqueSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class AgenceViewset(viewsets.ModelViewSet):
    queryset=Agence.objects.all()
    serializer_class=AgenceSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class FournisseurViewset(viewsets.ModelViewSet):
    queryset=Fournisseur.objects.all()
    serializer_class=FournisseurSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class RegionViewset(viewsets.ModelViewSet):
    queryset=Region.objects.all()
    serializer_class=RegionSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class ClientViewset(viewsets.ModelViewSet):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class ProspectionClientViewset(viewsets.ModelViewSet):
    queryset=ProspectionClient.objects.all()
    serializer_class=ProspectionClientSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class CompteBancaireViewset(viewsets.ModelViewSet):
    queryset=CompteBancaire.objects.all()
    serializer_class=CompteBancaireSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class TentativesViewset(viewsets.ModelViewSet):
    queryset=Tentatives.objects.all()
    serializer_class=TentativesSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
