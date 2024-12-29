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
from core.pagination import PageNumberPagination

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SelectStoreView(APIView):
    def post(self, request):
        store_id = request.data.get('store_id')
        storedata = store.objects.get(id=store_id)
        store_data = StoreSerializer(storedata).data
        for key, value in store_data.items():
            if isinstance(value, Decimal):
                store_data[key] = float(value)
        
        request.session["store"] = store_data
        return Response(store_data, status=status.HTTP_200_OK)





class storeViewset(viewsets.ModelViewSet):
    queryset=store.objects.all()
    serializer_class=StoreSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    


# Create your views here.
class JournalViewset(viewsets.ModelViewSet):
    queryset=Journal.objects.all()
    serializer_class=JournalSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class PlanComptableClassViewset(viewsets.ModelViewSet):
    queryset=PlanComptableClass.objects.all()
    serializer_class=PlanComptableClassSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class PlanComptableAccountViewset(viewsets.ModelViewSet):
    queryset=PlanComptableAccount.objects.all()
    serializer_class=PlanComptableAccountSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class CompteEntrepriseViewset(viewsets.ModelViewSet):
    queryset=CompteEntreprise.objects.all()
    serializer_class=CompteEntrepriseSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class TaxesViewset(viewsets.ModelViewSet):
    queryset=Taxes.objects.all()
    serializer_class=TaxesSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class ValeurDeviseViewset(viewsets.ModelViewSet):
    queryset=ValeurDevise.objects.all()
    serializer_class=ValeurDeviseSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class typeClientViewset(viewsets.ModelViewSet):
    queryset=typeClient.objects.all()
    serializer_class=typeClientSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class DeviseViewset(viewsets.ModelViewSet):
    queryset=Devise.objects.all()
    serializer_class=DeviseSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

