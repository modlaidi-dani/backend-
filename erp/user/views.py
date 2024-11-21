
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


class CustomGroupViewset(viewsets.ModelViewSet):
    queryset=CustomGroup.objects.all()
    serializer_class=CustomGroupSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
class CustomUserViewset(viewsets.ModelViewSet):
    queryset=CustomUser.objects.all()
    serializer_class=CustomUserSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
    

class EquipeViewset(viewsets.ModelViewSet):
    queryset=Equipe.objects.all()
    serializer_class=EquipeSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]