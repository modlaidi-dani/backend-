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


class RequeteSalarieViewset(viewsets.ModelViewSet):
    queryset=RequeteSalarie.objects.all()
    serializer_class=RequeteSalarieSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class EventViewset(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=EventSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class SalarieViewset(viewsets.ModelViewSet):
    queryset=Salarie.objects.all()
    serializer_class=SalarieSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class ReglementCompteViewset(viewsets.ModelViewSet):
    queryset=ReglementCompte.objects.all()
    serializer_class=ReglementCompteSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class CongeViewset(viewsets.ModelViewSet):
    queryset=Conge.objects.all()
    serializer_class=CongeSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class PointageViewset(viewsets.ModelViewSet):
    queryset=Pointage.objects.all()
    serializer_class=PointageSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class AvanceSalaireViewset(viewsets.ModelViewSet):
    queryset=AvanceSalaire.objects.all()
    serializer_class=AvanceSalaireSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class PrixSocialViewset(viewsets.ModelViewSet):
    queryset=PrixSocial.objects.all()
    serializer_class=PrixSocialSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class HeureSupViewset(viewsets.ModelViewSet):
    queryset=HeureSup.objects.all()
    serializer_class=HeureSupSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class PrimeMotivationViewset(viewsets.ModelViewSet):
    queryset=PrimeMotivation.objects.all()
    serializer_class=PrimeMotivationSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class AbsenceViewset(viewsets.ModelViewSet):
    queryset=Absence.objects.all()
    serializer_class=AbsenceSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class ContratViewset(viewsets.ModelViewSet):
    queryset=Contrat.objects.all()
    serializer_class=ContratSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class RenumerationViewset(viewsets.ModelViewSet):
    queryset=Renumeration.objects.all()
    serializer_class=RenumerationSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class BoiteArchiveViewset(viewsets.ModelViewSet):
    queryset=BoiteArchive.objects.all()
    serializer_class=BoiteArchiveSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]

