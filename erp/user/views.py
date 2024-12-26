
from django.shortcuts import render
from .models import * 
from .serializers import * 
# from permissions import *
from rest_framework import viewsets,views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser
from rest_framework import response,status
from rest_framework_simplejwt.authentication import JWTAuthentication
# from permissions import IsManager
from core.permission import DynamicPermission
from core.filters import  UserFilterBackend, StoreFilter
class UserActuel(views.APIView):
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        user = request.user  
        user = CustomUser.objects.filter(username=user.username).first()
        serializer = CustomUserSerializer(user)  
        return Response(serializer.data, status=status.HTTP_200_OK)
        

class UserCustomPermissionViewset(viewsets.ModelViewSet):
    queryset=CustomUser.objects.all()
    serializer_class=UserCustomPermissionSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
    filter_backends=[ UserFilterBackend, StoreFilter]


class CustomGroupViewset(viewsets.ModelViewSet):
    queryset=CustomGroup.objects.all()
    serializer_class=CustomGroupSerializer
    authentication_classes=[JWTAuthentication]
    filter_backends=[ UserFilterBackend, StoreFilter]

    permission_classes=[IsAuthenticated]
class CustomUserViewset(viewsets.ModelViewSet):
    queryset=CustomUser.objects.all()
    serializer_class=CustomUserSerializer
    authentication_classes=[JWTAuthentication]
    filter_backends=[ UserFilterBackend, StoreFilter]

    permission_classes=[IsAuthenticated]
    

class EquipeViewset(viewsets.ModelViewSet):
    queryset=Equipe.objects.all()
    serializer_class=EquipeSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
    filter_backends=[ UserFilterBackend, StoreFilter]

class cordinatesViewset(viewsets.ModelViewSet):
    queryset=cordinates.objects.all()
    serializer_class=cordinatesSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated]
    filter_backends=[ UserFilterBackend, StoreFilter]

    