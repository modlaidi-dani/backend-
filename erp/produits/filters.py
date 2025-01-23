import django_filters
from .models import *
from inventory.models import *
from django_filters import rest_framework as filters 
class ProduitFiltercategory(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        label="category"
    )
    class Meta:
        model = Product
        fields = {       
            'category':['exact']  
        }
class StockStateFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(
        field_name="product__category",
        queryset=Category.objects.all(),
        label="category"
    )
    entrepot = django_filters.ModelChoiceFilter(
        field_name="entrepot",
        queryset=Entrepot.objects.all(),
        label="entrepot"
    )

    class Meta:
        model = Stock
        fields = ['entrepot','category']  