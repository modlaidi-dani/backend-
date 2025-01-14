import django_filters
from .models import *
from clientInfo.models import typeClient
from user.models import *
class ClientFilter(django_filters.FilterSet):

    user = django_filters.ModelChoiceFilter(
        queryset=CustomUser.objects.all(),
        label="user"
    )


    categorie_client = django_filters.ModelChoiceFilter(
        queryset=typeClient.objects.all(),
        label="categorie_client"
    )
    class Meta:
        model = Client
        fields = [ 'user', 'categorie_client']