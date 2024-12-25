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

class ArchivageBonSortieViewset(viewsets.ModelViewSet):
    queryset=ArchivageBonSortie.objects.all()
    serializer_class=ArchivageBonSortieSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination
class ArchivageProduitsEnBonSortieViewset(viewsets.ModelViewSet):
    queryset=ArchivageProduitsEnBonSortie.objects.all()
    serializer_class=ArchivageProduitsEnBonSortieSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination