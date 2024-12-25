import django_filters
from .models import *

class ProduitFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        label="category"
    )
    class Meta:
        model = Product
        fields = {
            'reference': ['icontains'],          
            'name': ['icontains'],       
            'category':['exact']  
        }