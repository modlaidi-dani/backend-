import django_filters
from .models import *
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
