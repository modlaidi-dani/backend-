import django_filters
from .models import *

class AvanceSalaireFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name="date", lookup_expr="gte", label="Start Date")
    end_date = django_filters.DateFilter(field_name="date", lookup_expr="lte", label="End Date")

    class Meta:
        model = AvanceSalaire
        fields = [ 'start_date', 'end_date']
class PointageFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name="date", lookup_expr="gte", label="Start Date")
    end_date = django_filters.DateFilter(field_name="date", lookup_expr="lte", label="End Date")

    class Meta:
        model = Pointage
        fields = [ 'start_date', 'end_date']