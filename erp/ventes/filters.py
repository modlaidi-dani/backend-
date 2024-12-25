import django_filters
from .models import *
from tiers.models import *
from user.models import *
class BonSortieFilter(django_filters.FilterSet):
    client = django_filters.ModelChoiceFilter(
        queryset=Client.objects.all(),
        label="client"
    )
    user = django_filters.ModelChoiceFilter(
        queryset=CustomUser.objects.all(),
        label="user"
    )
    class Meta:
        model = BonSortie
        fields = {
            'idBon': ['idBon'],          
            'date': ['icontains'],       
            'client':['exact'],
            'user':['exact'],  
              
        }