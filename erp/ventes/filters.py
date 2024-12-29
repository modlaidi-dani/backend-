import django_filters
from .models import *
from produits.models import Category
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
    # idBon = django_filters.CharFilter(
    #     field_name="idBon",
    #     lookup_expr="icontains",  # Recherche insensible à la casse
    #     label="ID Bon"
    # )
    # produit_reference = django_filters.NumberFilter(
    #     field_name="produits_en_bon_sorties__reference", lookup_expr="icontains", label="Product reference"
    # )
    # produit_name = django_filters.NumberFilter(
    #     field_name="produits_en_bon_sorties__name", lookup_expr="icontains", label="Product name"
    # )
    produit_category = django_filters.ModelChoiceFilter(
        field_name="produits_en_bon_sorties__category",
        queryset=Category.objects.all(),
        label="Product Category"
    )
    class Meta:
        model = BonSortie
        fields = [ 'client', 'user', 'start_date', 'end_date','produit_category']