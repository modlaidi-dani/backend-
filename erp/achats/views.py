from django.shortcuts import render
from .models import * 
from .serializers import * 
# from permissions import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser
from rest_framework import response,status
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class BonCommandeAchatViewset(viewsets.ModelViewSet):
    queryset=BonCommandeAchat.objects.all()
    serializer_class=BonCommandeAchatSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
    
class ProduitsEnBonCommandesAchatViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnBonCommandesAchat.objects.all()
    serializer_class=ProduitsEnBonCommandesAchatSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
    
class DossierAchatViewset(viewsets.ModelViewSet):
    queryset=DossierAchat.objects.all()
    serializer_class=DossierAchatSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
    
class BonAchatViewset(viewsets.ModelViewSet):
    queryset=BonAchat.objects.all()
    serializer_class=BonAchatSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
    
class FactureAchatViewset(viewsets.ModelViewSet):
    queryset=FactureAchat.objects.all()
    serializer_class=FactureAchatSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
    
class ProduitsEnFactureAchatViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnFactureAchat.objects.all()
    serializer_class=ProduitsEnFactureAchatSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
    
class ProduitsEnBonAchatViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnBonAchat.objects.all()
    serializer_class=ProduitsEnBonAchatSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
    
class AvoirAchatViewset(viewsets.ModelViewSet):
    queryset=AvoirAchat.objects.all()
    serializer_class=AvoirAchatSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
    
class BonReceptionViewset(viewsets.ModelViewSet):
    queryset=BonReception.objects.all()
    serializer_class=BonReceptionSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class ExpeditionViewset(viewsets.ModelViewSet):
    queryset=Expedition.objects.all()
    serializer_class=ExpeditionSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]

class ProduitsEnBonReceptionViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnBonReception.objects.all()
    serializer_class=ProduitsEnBonReceptionSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class ProjetCreditViewset(viewsets.ModelViewSet):
    queryset=ProjetCredit.objects.all()
    serializer_class=ProjetCreditSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class CreditNoteViewset(viewsets.ModelViewSet):
    queryset=CreditNote.objects.all()
    serializer_class=CreditNoteSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class ProduitsEnCreditNoteViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnCreditNote.objects.all()
    serializer_class=ProduitsEnCreditNoteSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]