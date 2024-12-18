from django.shortcuts import render
from .models import * 
from .serializers import * 
# from permissions import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser
from rest_framework import response,status
from rest_framework_simplejwt.authentication import JWTAuthentication
from core.permission import DynamicPermission
from core.filters import UserFilterBackend
# Create your views here.

class BonCommandeAchatViewset(viewsets.ModelViewSet):
    queryset=BonCommandeAchat.objects.all()
    serializer_class=BonCommandeAchatSerializer
    authentication_classes=[JWTAuthentication]
    filterset_class=[UserFilterBackend]
    permission_classes=[IsAuthenticated,DynamicPermission]
    def create(self, request, *args, **kwargs):
        data=request.data
        year = '24'
        last_avoir = models.AvoirAchat.objects.last()

        if last_avoir:
            last_code = last_avoir.codeAvoir
            last_sequence = int(last_code.split('-')[1])
            next_sequence = last_sequence + 1
        else:
            next_sequence = 1
        codeAvoir = f"AV{year}-{next_sequence:03d}"
        data["codeAvoir"]=codeAvoir
        serializer=self.get_seralizer(data=data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class ProduitsEnBonCommandesAchatViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnBonCommandesAchat.objects.all()
    serializer_class=ProduitsEnBonCommandesAchatSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated,DynamicPermission]
    filterset_class=[UserFilterBackend]
    
    
class DossierAchatViewset(viewsets.ModelViewSet):
    queryset=DossierAchat.objects.all()
    serializer_class=DossierAchatSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated,DynamicPermission]
    filterset_class=[UserFilterBackend]
    
    
class BonAchatViewset(viewsets.ModelViewSet):
    queryset=BonAchat.objects.all()
    serializer_class=BonAchatSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated,DynamicPermission]
    filterset_class=[UserFilterBackend]
    
    
class FactureAchatViewset(viewsets.ModelViewSet):
    queryset=FactureAchat.objects.all()
    serializer_class=FactureAchatSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated,DynamicPermission]
    filterset_class=[UserFilterBackend]
    
    
class ProduitsEnFactureAchatViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnFactureAchat.objects.all()
    serializer_class=ProduitsEnFactureAchatSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated,DynamicPermission]
    filterset_class=[UserFilterBackend]
    
    
class ProduitsEnBonAchatViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnBonAchat.objects.all()
    serializer_class=ProduitsEnBonAchatSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated,DynamicPermission]
    filterset_class=[UserFilterBackend]
    
    
class AvoirAchatViewset(viewsets.ModelViewSet):
    queryset=AvoirAchat.objects.all()
    serializer_class=AvoirAchatSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated,DynamicPermission]
    filterset_class=[UserFilterBackend]
    
    
class BonReceptionViewset(viewsets.ModelViewSet):
    queryset=BonReception.objects.all()
    serializer_class=BonReceptionSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated,DynamicPermission]
    filterset_class=[UserFilterBackend]

class ExpeditionViewset(viewsets.ModelViewSet):
    queryset=Expedition.objects.all()
    serializer_class=ExpeditionSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated,DynamicPermission]
    filterset_class=[UserFilterBackend]


class ProduitsEnBonReceptionViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnBonReception.objects.all()
    serializer_class=ProduitsEnBonReceptionSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated,DynamicPermission]
    filterset_class=[UserFilterBackend]

class ProjetCreditViewset(viewsets.ModelViewSet):
    queryset=ProjetCredit.objects.all()
    serializer_class=ProjetCreditSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated,DynamicPermission]
    filterset_class=[UserFilterBackend]

class CreditNoteViewset(viewsets.ModelViewSet):
    queryset=CreditNote.objects.all()
    serializer_class=CreditNoteSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated,DynamicPermission]
    filterset_class=[UserFilterBackend]

class ProduitsEnCreditNoteViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnCreditNote.objects.all()
    serializer_class=ProduitsEnCreditNoteSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated,DynamicPermission]
    filterset_class=[UserFilterBackend]

