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


class ProduitsEnBonCommandeViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnBonCommande.objects.all()
    serializer_class=ProduitsEnBonCommandeSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class FactureViewset(viewsets.ModelViewSet):
    queryset=Facture.objects.all()
    serializer_class=FactureSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class AvoirVenteViewset(viewsets.ModelViewSet):
    queryset=AvoirVente.objects.all()
    serializer_class=AvoirVenteSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class validationBlViewset(viewsets.ModelViewSet):
    queryset=validationBl.objects.all()
    serializer_class=validationBlSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class BonSortieViewset(viewsets.ModelViewSet):
    queryset=BonSortie.objects.all()
    serializer_class=BonSortieSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class DemandeTransfertViewset(viewsets.ModelViewSet):
    queryset=DemandeTransfert.objects.all()
    serializer_class=DemandeTransfertSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class ConfirmationBlViewset(viewsets.ModelViewSet):
    queryset=ConfirmationBl.objects.all()
    serializer_class=ConfirmationBlSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class ProduitsEnBonSortieViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnBonSortie.objects.all()
    serializer_class=ProduitsEnBonSortieSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class BonGarantieViewset(viewsets.ModelViewSet):
    queryset=BonGarantie.objects.all()
    serializer_class=BonGarantieSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class ProduitsEnBonGarantieViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnBonGarantie.objects.all()
    serializer_class=ProduitsEnBonGarantieSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class BonDevisViewset(viewsets.ModelViewSet):
    queryset=BonDevis.objects.all()
    serializer_class=BonDevisSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class ProduitsEnBonDevisViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnBonDevis.objects.all()
    serializer_class=ProduitsEnBonDevisSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class BonCommandeViewset(viewsets.ModelViewSet):
    queryset=BonCommande.objects.all()
    serializer_class=BonCommandeSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class ProduitsEnFactureViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnFacture.objects.all()
    serializer_class=ProduitsEnFactureSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
