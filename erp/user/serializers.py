from rest_framework import serializers
from .models import *
from clientInfo.serializers import *
from inventory.serializers import *


class UserCustomPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserCustomPermission
        fields="__all__"
class GroupePermissionSerializer(serializers.ModelSerializer):
    permissions=UserCustomPermissionSerializer(many=True,source="users_permissions")
    class Meta:
        model=GroupePermission
        fields="__all__"
class CustomGroupSerializer(serializers.ModelSerializer):
    permissions_groupe=GroupePermissionSerializer(many=True)
    class Meta:
        model=CustomGroup
        fields="__all__"
class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Equipe
        fields="__all__"
class cordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model=cordinates
        fields="__all__"
class CustomUserSerializer(serializers.ModelSerializer):
    # permission=UserCustomPermissionSerializer()
    group=CustomGroupSerializer()
    # EmployeeAt=StoreSerializer()
    # # entrepots_responsible=EntrepotSerializer()
    # equipe_affiliated=EquipeSerializer()
    class Meta:
        model=CustomUser
        fields="__all__"
    def to_internal_value(self, data):
        user=self.context['request'].user
        internal_value = super().to_internal_value(data)
        Username=internal_value["username"]
        Password=internal_value["password"]
        first_name=internal_value["first_name"]
        last_name=internal_value["last_name"]
        email=internal_value["email"]
        datauser=dict(
            username=Username,
            password=Password,
            first_name=first_name,
            last_name=last_name,
            email=email, 
        )
        # Récupérer le mot de passe et le hacher
        if 'password' in datauser:
            password = datauser.pop('password')
            # Hacher le mot de passe
            user = User(**datauser)
            user.set_password(password)
            internal_value['password'] = user.password  # Conserver le mot de passe haché
        return internal_value    
    