import django_filters
from .models import *
from inventory.models import Entrepot
from clientInfo.models import CompteEntreprise
class ClotureFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name="date", lookup_expr="gte", label="Start Date")
    end_date = django_filters.DateFilter(field_name="date", lookup_expr="lte", label="End Date")
    user = django_filters.ModelChoiceFilter(
        field_name="user",
        queryset=CustomUser.objects.all(),
        label="user"
    )
    caisse = django_filters.ModelChoiceFilter(
        field_name="caisse",
        queryset=CompteEntreprise.objects.none(),
        label="Caisse"
    )

    class Meta:
        model = Cloture
        fields = ['start_date', 'end_date', 'caisse']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Récupérer tous les utilisateurs liés à des enregistrements dans Cloture
        utilisateurs_ids = Cloture.objects.values_list('user', flat=True).distinct()

        # Récupérer les comptes liés via AffectationCaisse pour ces utilisateurs
        caisses_ids = AffectationCaisse.objects.filter(
            utilisateur__id__in=utilisateurs_ids
        ).values_list('CompteTres', flat=True).distinct()

        # Mettre à jour le queryset pour le filtre `caisse`
        self.filters['caisse'].queryset = CompteEntreprise.objects.filter(id__in=caisses_ids)