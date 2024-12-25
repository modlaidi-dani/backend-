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
    start_date = django_filters.DateFilter(field_name="dateBon", lookup_expr="gte", label="Start Date")
    end_date = django_filters.DateFilter(field_name="dateBon", lookup_expr="lte", label="End Date")
    idBon = django_filters.CharFilter(
        field_name="idBon",
        lookup_expr="icontains",  # Recherche insensible à la casse
        label="ID Bon"
    )
    class Meta:
        model = BonSortie
        fields = ['idBon', 'client', 'user', 'start_date', 'end_date']