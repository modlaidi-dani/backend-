
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
class permissionsToGroupe(views.APIView):
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAuthenticated, DynamicPermission]
    def post(self, request):
        groupe_id = request.data.get('group_id')  
        permissions_ids = request.data.get('groupe_permissions', [])  
        try:
            groupe = CustomGroup.objects.get(id=groupe_id)
        except CustomGroup.DoesNotExist:
            return Response({"error": "Group not found"}, status=status.HTTP_404_NOT_FOUND)
        permissions = GroupePermission.objects.filter(id__in=permissions_ids)
        groupe.permissions_groupe.set(permissions)  
        return Response({"message": "Permissions updated for the group"}, status=status.HTTP_200_OK)
class permissionsToUser(views.APIView):
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAuthenticated, DynamicPermission]
    def post(self, request):
        user_id = request.data.get('user_id')  
        permissions_ids = request.data.get('user_permissions', [])  
        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response({"error": "user not found"}, status=status.HTTP_404_NOT_FOUND)
        permissions = UserCustomPermission.objects.filter(id__in=permissions_ids)
        user.permission.set(permissions)  
        return Response({"message": "Permissions updated for the group"}, status=status.HTTP_200_OK)       
        
class UserActuel(views.APIView):
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAuthenticated, DynamicPermission]
    def get(self, request, *args, **kwargs):
        user = request.user  
        user = CustomUser.objects.filter(username=user.username).first()
        serializer = CustomUserSerializer(user)  
        return Response(serializer.data, status=status.HTTP_200_OK)
        

class UserCustomPermissionViewset(viewsets.ModelViewSet):
    queryset=UserCustomPermission.objects.all()
    serializer_class=UserCustomPermissionSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission]
    filter_backends=[ UserFilterBackend, StoreFilter]
class GroupePermissionViewset(viewsets.ModelViewSet):
    queryset=GroupePermission.objects.all()
    serializer_class=GroupePermissionSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission]
    filter_backends=[ UserFilterBackend, StoreFilter]

class CustomGroupViewset(viewsets.ModelViewSet):
    queryset=CustomGroup.objects.all()
    serializer_class=CustomGroupSerializer
    authentication_classes=[JWTAuthentication]
    filter_backends=[ UserFilterBackend, StoreFilter]

    permission_classes=[IsAuthenticated, DynamicPermission]
class CustomUserViewset(viewsets.ModelViewSet):
    queryset=CustomUser.objects.all()
    serializer_class=CustomUserSerializer
    authentication_classes=[JWTAuthentication]
    filter_backends=[ UserFilterBackend, StoreFilter]

    permission_classes=[IsAuthenticated, DynamicPermission]
    

class EquipeViewset(viewsets.ModelViewSet):
    queryset=Equipe.objects.all()
    serializer_class=EquipeSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission]
    filter_backends=[ UserFilterBackend, StoreFilter]

class cordinatesViewset(viewsets.ModelViewSet):
    queryset=cordinates.objects.all()
    serializer_class=cordinatesSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission]
    filter_backends=[ UserFilterBackend, StoreFilter]

    