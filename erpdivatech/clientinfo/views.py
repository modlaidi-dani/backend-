from django.shortcuts import render
from .models import * 
from .serialisers import * 
# from permissions import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser
from rest_framework import response,status
from rest_framework_simplejwt.authentication import JWTAuthentication
# from permissions import IsManager


class storeViewset(viewsets.ModelViewSet):
    queryset=store.objects.all()
    serializer_class=StoreSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]

# Create your views here.
class JournalViewset(viewsets.ModelViewSet):
    queryset=Journal.objects.all()
    serializer_class=JournalSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class PlanComptableClassViewset(viewsets.ModelViewSet):
    queryset=PlanComptableClass.objects.all()
    serializer_class=PlanComptableClassSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class PlanComptableAccountViewset(viewsets.ModelViewSet):
    queryset=PlanComptableAccount.objects.all()
    serializer_class=PlanComptableAccountSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class CompteEntrepriseViewset(viewsets.ModelViewSet):
    queryset=CompteEntreprise.objects.all()
    serializer_class=CompteEntrepriseSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class TaxesViewset(viewsets.ModelViewSet):
    queryset=Taxes.objects.all()
    serializer_class=TaxesSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class ValeurDeviseViewset(viewsets.ModelViewSet):
    queryset=ValeurDevise.objects.all()
    serializer_class=ValeurDeviseSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class typeClientViewset(viewsets.ModelViewSet):
    queryset=typeClient.objects.all()
    serializer_class=typeClientSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class DeviseViewset(viewsets.ModelViewSet):
    queryset=Devise.objects.all()
    serializer_class=DeviseSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]