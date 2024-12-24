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


class ordreFabricationViewset(viewsets.ModelViewSet):
    queryset=ordreFabrication.objects.all()
    serializer_class=ordreFabricationSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]


class ProduitsEnOrdreFabricationViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnOrdreFabrication.objects.all()
    serializer_class=ProduitsEnOrdreFabricationSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]


class ProduitProductionBLViewset(viewsets.ModelViewSet):
    queryset=ProduitProductionBL.objects.all()
    serializer_class=ProduitProductionBLSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]


class ProduitProductionFacViewset(viewsets.ModelViewSet):
    queryset=ProduitProductionFac.objects.all()
    serializer_class=ProduitProductionFacSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]
