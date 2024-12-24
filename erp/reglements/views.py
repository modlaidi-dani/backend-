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

class ModeReglementViewset(viewsets.ModelViewSet):
    queryset=ModeReglement.objects.all()
    serializer_class=ModeReglementSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]

class depenseViewset(viewsets.ModelViewSet):
    queryset=depense.objects.all()
    serializer_class=depenseSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]

class EcheanceReglementViewset(viewsets.ModelViewSet):
    queryset=EcheanceReglement.objects.all()
    serializer_class=EcheanceReglementSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]

class HistoriqueMontantRecupererViewset(viewsets.ModelViewSet):
    queryset=HistoriqueMontantRecuperer.objects.all()
    serializer_class=HistoriqueMontantRecupererSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]

class ReglementViewset(viewsets.ModelViewSet):
    queryset=Reglement.objects.all()
    serializer_class=ReglementSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]

class ReglementFournisseurViewset(viewsets.ModelViewSet):
    queryset=ReglementFournisseur.objects.all()
    serializer_class=ReglementFournisseurSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]

class ClotureReglementsViewset(viewsets.ModelViewSet):
    queryset=ClotureReglements.objects.all()
    serializer_class=ClotureReglementsSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]

class montantCollectedViewset(viewsets.ModelViewSet):
    queryset=montantCollected.objects.all()
    serializer_class=montantCollectedSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]

class mouvementCaisseViewset(viewsets.ModelViewSet):
    queryset=mouvementCaisse.objects.all()
    serializer_class=mouvementCaisseSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]

class TypeDepenseViewset(viewsets.ModelViewSet):
    queryset=TypeDepense.objects.all()
    serializer_class=TypeDepenseSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]

