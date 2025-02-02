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



class pointVenteViewset(viewsets.ModelViewSet):
    queryset=pointVente.objects.all()
    serializer_class=pointVenteSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend, StoreFilter]

class EmplacementViewset(viewsets.ModelViewSet):
    queryset=Emplacement.objects.all()
    serializer_class=EmplacementSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend, StoreFilter]

class AffectationCaisseViewset(viewsets.ModelViewSet):
    queryset=AffectationCaisse.objects.all()
    serializer_class=AffectationCaisseSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend, StoreFilter]

class ClotureViewset(viewsets.ModelViewSet):
    queryset=Cloture.objects.all()
    serializer_class=ClotureSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend, StoreFilter]

class BonComptoireViewset(viewsets.ModelViewSet):
    queryset=BonComptoire.objects.all()
    serializer_class=BonComptoireSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend, StoreFilter]

class BonRectificationViewset(viewsets.ModelViewSet):
    queryset=BonRectification.objects.all()
    serializer_class=BonRectificationSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend, StoreFilter]

class verssementViewset(viewsets.ModelViewSet):
    queryset=verssement.objects.all()
    serializer_class=verssementSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend, StoreFilter]

class BonRetourComptoirViewset(viewsets.ModelViewSet):
    queryset=BonRetourComptoir.objects.all()
    serializer_class=BonRetourComptoirSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend, StoreFilter]

class ProduitsEnBonRetourComptoirViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnBonRetourComptoir.objects.all()
    serializer_class=ProduitsEnBonRetourComptoirSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend, StoreFilter]

class ProduitsEnBonRectifViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnBonRectif.objects.all()
    serializer_class=ProduitsEnBonRectifSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend, StoreFilter]

class ProduitsEnBonComptoirViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnBonComptoir.objects.all()
    serializer_class=ProduitsEnBonComptoirSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend, StoreFilter]

    