from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import * 
from .serializers import * 
# from permissions import *
from rest_framework import viewsets, views ,generics 
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser
from rest_framework import response,status
from rest_framework_simplejwt.authentication import JWTAuthentication
# from permissions import IsManager
from rest_framework.filters import SearchFilter
from core.permission import DynamicPermission
from core.filters import  UserFilterBackend, StoreFilter
from core.pagination import PageNumberPagination
from .filters import *
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models.functions import Lower
from ventes.models import *
from datetime import datetime, timedelta

class CategoryViewset(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend, StoreFilter]
    pagination_class = PageNumberPagination 

class ProductViewset(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[SearchFilter,DjangoFilterBackend, UserFilterBackend,  StoreFilter]
    pagination_class = PageNumberPagination 
    filterset_class=ProduitFiltercategory
    search_fields = ['name', 'reference']
    

class HistoriqueAchatProduitViewset(viewsets.ModelViewSet):
    queryset=HistoriqueAchatProduit.objects.all()
    serializer_class=HistoriqueAchatProduitSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend,  StoreFilter]
    pagination_class = PageNumberPagination 
    

class NumSeriesViewset(viewsets.ModelViewSet):
    queryset=NumSeries.objects.all()
    serializer_class=NumSeriesSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend,  StoreFilter]
    pagination_class = PageNumberPagination 
    

class variantsPrixClientViewset(viewsets.ModelViewSet):
    queryset=variantsPrixClient.objects.all()
    serializer_class=variantsPrixClientSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend,  StoreFilter]
    pagination_class = PageNumberPagination 
    

class PromotionViewset(viewsets.ModelViewSet):
    queryset=Promotion.objects.all()
    serializer_class=PromotionSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend,  StoreFilter]
    pagination_class = PageNumberPagination 
    

class Variantes_productViewset(viewsets.ModelViewSet):
    queryset=Variantes_product.objects.all()
    serializer_class=Variantes_productSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend,  StoreFilter]
    pagination_class = PageNumberPagination 
    

class ProductVariantViewset(viewsets.ModelViewSet):
    queryset=ProductVariant.objects.all()
    serializer_class=ProductVariantSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend,  StoreFilter]
    pagination_class = PageNumberPagination 
    

class historique_prix_achatViewset(viewsets.ModelViewSet):
    queryset=historique_prix_achat.objects.all()
    serializer_class=historique_prix_achatSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend,  StoreFilter]
    pagination_class = PageNumberPagination 
    

class VerificationArchiveViewset(viewsets.ModelViewSet):
    queryset=VerificationArchive.objects.all()
    serializer_class=VerificationArchiveSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend,  StoreFilter]
    pagination_class = PageNumberPagination 
    

class ListProductVerificationArchiveViewset(viewsets.ModelViewSet):
    queryset=ListProductVerificationArchive.objects.all()
    serializer_class=ListProductVerificationArchiveSerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend,  StoreFilter]
    pagination_class = PageNumberPagination 
    


class codeEAViewset(viewsets.ModelViewSet):
    queryset=codeEA.objects.all()
    serializer_class=codeEASerializer
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend,  StoreFilter]
    pagination_class = PageNumberPagination 
    

class EtatStockViewset(generics.GenericAPIView):
    authentication_classes=[JWTAuthentication] 
    permission_classes=[IsAuthenticated, DynamicPermission ]
    filter_backends=[ UserFilterBackend,  StoreFilter]
    pagination_class = PageNumberPagination
    def get(self, request):
        selected_store = store.objects.get(pk=self.request.session["store"])
        products = Product.objects.filter(
            store=selected_store,
            parent_product__isnull=True,
            name__icontains='msi'
        ).annotate(
            name_lower=Lower('name')
        ).filter(
            name_lower__icontains='msi'
        )
        products_stock = []
        for product in products:
            report = []
            initial_quantity = sum(stock.quantity_initial for stock in product.mon_stock.all())
            current_year = datetime.now().year
            start_date = datetime(current_year, 1, 1)
            end_date_onyear = datetime(current_year, 12, 31)
            total_weeks = (end_date_onyear - start_date).days // 7 + 1
            for week in range(1, total_weeks + 1):
                end_date = start_date + timedelta(days=6)
                entered_quantity= ProduitsEnBonEntry.objects.filter(
                                                stock=product,
                                                BonNo__dateBon__range=[start_date, end_date]
                                            ).aggregate(models.Sum('quantity'))['quantity__sum'] or 0
                produits_en_bon_sortie_list = ProduitsEnBonSortie.objects.filter(
                            stock=product,
                            BonNo__dateBon__range=[start_date, end_date]
                        )

                filtered_produits_en_bon_sortie = [
                    produit_en_bon_sortie for produit_en_bon_sortie in produits_en_bon_sortie_list
                    if produit_en_bon_sortie.BonNo.get_etat_transfert
                ]

                sold_quantity = sum(produit_en_bon_sortie.quantity for produit_en_bon_sortie in filtered_produits_en_bon_sortie)
                returned_quantity = ProduitsEnBonRetour.objects.filter(
                            produit=product,
                            reintegrated =True,
                            BonNo__dateBon__range=[start_date, end_date]
                        ).aggregate(models.Sum('quantity'))['quantity__sum'] or 0
                final_quantity = initial_quantity + entered_quantity - sold_quantity + returned_quantity 
                report.append({
                    'week': week,
                    'start_date': start_date.strftime('%Y-%m-%d'),
                    'end_date': end_date.strftime('%Y-%m-%d'),
                    'reference': product.reference,
                    'name': product.name,
                    'categorie': product.category.pc_component if product.category else '',
                    'initial_quantity': initial_quantity,
                    'entered_quantity': entered_quantity,
                    'sold_quantity': sold_quantity,
                    'final_quantity': final_quantity,
                    'returned_quantity': returned_quantity,
                })

                # Update the initial quantity for the next week
                initial_quantity = final_quantity

                # Move to the next week
                start_date = end_date + timedelta(days=1)
            products_stock.extend(report)
        paginated_products_stock = self.paginate_queryset(products_stock)
        return self.get_paginated_response(paginated_products_stock)