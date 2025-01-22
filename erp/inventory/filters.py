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
class StockFilter(django_filters.FilterSet):

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
        fields = ['category','entrepot']    
class BonentyFilter(django_filters.FilterSet):

    start_date = django_filters.DateFilter(field_name="dateBon", lookup_expr="gte", label="Start Date")
    end_date = django_filters.DateFilter(field_name="dateBon", lookup_expr="lte", label="End Date")
    entrepot = django_filters.ModelChoiceFilter(
        field_name="entrepot",
        queryset=Entrepot.objects.all(),
        label="entrepot"
    )
    # The `fournisseur` in the `BonentyFilter` class is a `django_filters.ModelChoiceFilter` that
    # filters the queryset based on the `fournisseur` field of the `BonEntry` model. It allows users
    # to select a specific `fournisseur` (supplier) when filtering instances of the `BonEntry` model.
    # The filter will display a dropdown list of available `Fournisseur` objects for selection.
    fournisseur = django_filters.ModelChoiceFilter(
        field_name="fournisseur",
        queryset=Fournisseur.objects.all(),
        label="fournisseur"
    )
    class Meta:
        model = BonEntry
        fields = ['start_date','fournisseur', 'end_date','entrepot']    