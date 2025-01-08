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
from core.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class RequeteSalarieViewset(viewsets.ModelViewSet):
    queryset=RequeteSalarie.objects.all()
    serializer_class=RequeteSalarieSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend, StoreFilter]

class EventViewset(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=EventSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend, StoreFilter]

class SalarieViewset(viewsets.ModelViewSet):
    queryset=Salarie.objects.all()
    serializer_class=SalarieSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends = [SearchFilter, DjangoFilterBackend, UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination
    search_fields = ['nom']

class ReglementCompteViewset(viewsets.ModelViewSet):
    queryset=ReglementCompte.objects.all()
    serializer_class=ReglementCompteSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends = [SearchFilter, DjangoFilterBackend, UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination
    search_fields = ['salarie__nom']

class CongeViewset(viewsets.ModelViewSet):
    queryset=Conge.objects.all()
    serializer_class=CongeSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends = [SearchFilter, DjangoFilterBackend, UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination
    search_fields = ['salarie__nom']

class PointageViewset(viewsets.ModelViewSet):
    queryset=Pointage.objects.all()
    serializer_class=PointageSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends = [SearchFilter, DjangoFilterBackend, UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination
    search_fields = ['salarie__nom']

class AvanceSalaireViewset(viewsets.ModelViewSet):
    queryset=AvanceSalaire.objects.all()
    serializer_class=AvanceSalaireSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends = [SearchFilter, DjangoFilterBackend, UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination
    search_fields = ['salarie__nom']

class PrixSocialViewset(viewsets.ModelViewSet):
    queryset=PrixSocial.objects.all()
    serializer_class=PrixSocialSerializer
    authentication_classes=[JWTAuthentication] 
    filter_backends = [SearchFilter, DjangoFilterBackend, UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination
    search_fields = ['salarie__nom']

class HeureSupViewset(viewsets.ModelViewSet):
    queryset=HeureSup.objects.all()
    serializer_class=HeureSupSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends = [SearchFilter, DjangoFilterBackend, UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination
    search_fields = ['salarie__nom']

class PrimeMotivationViewset(viewsets.ModelViewSet):
    queryset=PrimeMotivation.objects.all()
    serializer_class=PrimeMotivationSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend, StoreFilter]

class AbsenceViewset(viewsets.ModelViewSet):
    queryset=Absence.objects.all()
    serializer_class=AbsenceSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend, StoreFilter]

class ContratViewset(viewsets.ModelViewSet):
    queryset=Contrat.objects.all()
    serializer_class=ContratSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend, StoreFilter]

class RenumerationViewset(viewsets.ModelViewSet):
    queryset=Renumeration.objects.all()
    serializer_class=RenumerationSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend, StoreFilter]

class BoiteArchiveViewset(viewsets.ModelViewSet):
    queryset=BoiteArchive.objects.all()
    serializer_class=BoiteArchiveSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend, StoreFilter]


