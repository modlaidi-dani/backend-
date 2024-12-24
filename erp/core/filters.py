from django_filters.rest_framework import DjangoFilterBackend
from user.models import *
class  UserFilterBackend(DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        user = request.user
        user_fields = ['user','User', 'utilisateur', 'chauffeur', 'author']
        for field in user_fields:
            if hasattr(queryset.model, field):
                costumeruser=CustomUser.objects.get(username=user)
                groups = costumeruser.group
                if groups.name.strip().lower() == "manager":
                    return queryset  
                filter_kwargs = {field: costumeruser}
                return queryset.filter(**filter_kwargs)
        return queryset
class StoreFilter(DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        user=request.user
        costumeruser=CustomUser.objects.get(username=user)
        if costumeruser.EmployeeAt:
            return queryset.filter(store=costumeruser.EmployeeAt)
        else:
            return queryset.filter(store=request.session.get('store'))
        return queryset