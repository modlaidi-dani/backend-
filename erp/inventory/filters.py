import django_filters
from .models import *
from produits.models import Category
from tiers.models import *
from user.models import *
class BonRetourFilter(django_filters.FilterSet):

    user = django_filters.ModelChoiceFilter(
        queryset=CustomUser.objects.all(),
        label="user"
    )
    start_date = django_filters.DateFilter(field_name="dateBon", lookup_expr="gte", label="Start Date")
    end_date = django_filters.DateFilter(field_name="dateBon", lookup_expr="lte", label="End Date")

    produit_category = django_filters.ModelChoiceFilter(
        field_name="produits_en_bon_sorties__category",
        queryset=Category.objects.all(),
        label="Product Category"
    )
    class Meta:
        model = BonRetour
        fields = [ 'user', 'start_date', 'end_date','produit_category']