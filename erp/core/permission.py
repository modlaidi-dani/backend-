from rest_framework.permissions import BasePermission
from user.models import *
class DynamicPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        view_name = view.__class__.__name__
        action = request.method.lower()

        try:
            user = CustomUser.objects.get(username=request.user.username)
        except CustomUser.DoesNotExist:
            return False
        group = user.group
        if user.role == "manager":
            permission_groupe=group.permissions_groupe.filter(views=view_name).first()

            if  not permission_groupe :
                permission_groupe = GroupePermission.objects.create(
                    views=view_name,
                    name= f"acces a {view_name}"
                )
                group.permissions_groupe.add(permission_groupe)

                actions = ['get', 'post', 'put', 'patch', 'delete']
                for act in actions:
                    name = f"peut {act} {view_name}"
                    permissionuser=UserCustomPermission.objects.create(
                        groupe=permission_groupe,
                        action=act,
                        name=name
                    )
                    user.permission.add(permissionuser)

            permission = user.permission.filter(action=action,groupe=permission_groupe)
        else:
            permission_groupe=group.permissions_groupe.filter(views=view_name).first()
            permission = user.permission.filter(action=action,groupe=permission_groupe)
            
        if permission:
            return True

        return False