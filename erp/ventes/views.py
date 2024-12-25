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
from .filters import *
from archivage.models import *
from datetime import datetime
class ProduitsEnBonCommandeViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnBonCommande.objects.all()
    serializer_class=ProduitsEnBonCommandeSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class FactureViewset(viewsets.ModelViewSet):
    queryset=Facture.objects.all()
    serializer_class=FactureSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination
    def perform_update(self, serializer):
        instance = self.get_object()
        user = self.request.user
        produits=isinstance.produits_en_facture.all()
        bon_archiv=ArchivageFacture.objects.create(
            facture=instance,  
            codeFacture=instance.codeFacture,
            date_facture=instance.date_facture,
            client=instance.client,
            BonS=instance.BonS,
            user=instance.user,
            mode_reglement=instance.mode_reglement,
            echeance_reglement=instance.echeance_reglement,
            banque_Reglement=instance.banque_Reglement,
            num_cheque_reglement=instance.num_cheque_reglement,
            Remise=instance.Remise,
            etat_reglement=instance.etat_reglement,
            shippingCost=instance.shippingCost,
            totalPrice=instance.totalPrice,
            valide=instance.valide,
            ferme=instance.ferme,
            regle=instance.regle,
            store=instance.store,
            user_update=user,
            date_update=datetime.now()
        )
        for produit in produits:
            ArchivageProduitsEnFacture.objects.create(
                facture_archiv=bon_archiv,  
                produitsfacture=produit,
                FactureNo=produit.FactureNo,  
                stock=produit.stock,  
                quantity=produit.quantity,
                unitprice=produit.unitprice,
                totalprice=produit.totalprice,
            )
        serializer.save() 

class AvoirVenteViewset(viewsets.ModelViewSet):
    queryset=AvoirVente.objects.all()
    serializer_class=AvoirVenteSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
class AvoirVenteAncienViewset(viewsets.ModelViewSet):
    queryset=AvoirVenteAncien.objects.all()
    serializer_class=AvoirVenteAncienSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
class produitsEnAvoirViewset(viewsets.ModelViewSet):
    queryset=produitsEnAvoir.objects.all()
    serializer_class=produitsEnAvoirSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
class produitsEnAvoirAViewset(viewsets.ModelViewSet):
    queryset=produitsEnAvoirA.objects.all()
    serializer_class=produitsEnAvoirASerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 

class validationBlViewset(viewsets.ModelViewSet):
    queryset=validationBl.objects.all()
    serializer_class=validationBlSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class BonSortieViewset(viewsets.ModelViewSet):
    queryset=BonSortie.objects.all()
    serializer_class=BonSortieSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ DjangoFilterBackend, UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination
    filterset_class=BonSortieFilter 
    def perform_update(self, serializer):
        instance = self.get_object()
        user = self.request.user
        produits=isinstance.produits_en_bon_sorties.all()
        bon_archiv=ArchivageBonSortie.objects.create(
            bon_sortie=instance,  
            idBon=instance.idBon,
            dateBon=instance.dateBon,
            client=instance.client,
            totalPrice=instance.totalPrice,
            user=instance.user,
            entrepot=instance.entrepot,
            mode_reglement=instance.mode_reglement,
            echeance_reglement=instance.echeance_reglement,
            banque_Reglement=instance.banque_Reglement,
            num_cheque_reglement=instance.num_cheque_reglement,
            Remise=instance.Remise,
            etat_reglement=instance.etat_reglement,
            shippingCost=instance.shippingCost,
            valide=instance.valide,
            ferme=instance.ferme,
            modifiable=instance.modifiable,
            confirmed=instance.confirmed,
            livre=instance.livre,
            typebl=instance.typebl,
            reference_pc=instance.reference_pc,
            name_pc=instance.name_pc,
            store=instance.store,
            user_update=user,
            date_update=datetime.now()
        )
        for produit in produits:
            ArchivageProduitsEnBonSortie.objects.create(
                produitsenbs=produit,  
                bon_archiv=bon_archiv,
                bon_sortie=produit.BonNo,  
                stock=produit.stock,  
                kit=produit.kit,
                quantity=produit.quantity,
                unitprice=produit.unitprice,
                totalprice=produit.totalprice,
                entrepot=produit.entrepot,
            )
        serializer.save()
        

class DemandeTransfertViewset(viewsets.ModelViewSet):
    queryset=DemandeTransfert.objects.all()
    serializer_class=DemandeTransfertSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]

class ConfirmationBlViewset(viewsets.ModelViewSet):
    queryset=ConfirmationBl.objects.all()
    serializer_class=ConfirmationBlSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class ProduitsEnBonSortieViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnBonSortie.objects.all()
    serializer_class=ProduitsEnBonSortieSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination
    

class BonGarantieViewset(viewsets.ModelViewSet):
    queryset=BonGarantie.objects.all()
    serializer_class=BonGarantieSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class ProduitsEnBonGarantieViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnBonGarantie.objects.all()
    serializer_class=ProduitsEnBonGarantieSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class BonDevisViewset(viewsets.ModelViewSet):
    queryset=BonDevis.objects.all()
    serializer_class=BonDevisSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class ProduitsEnBonDevisViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnBonDevis.objects.all()
    serializer_class=ProduitsEnBonDevisSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class BonCommandeViewset(viewsets.ModelViewSet):
    queryset=BonCommande.objects.all()
    serializer_class=BonCommandeSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

class ProduitsEnFactureViewset(viewsets.ModelViewSet):
    queryset=ProduitsEnFacture.objects.all()
    serializer_class=ProduitsEnFactureSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated ]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 
    

