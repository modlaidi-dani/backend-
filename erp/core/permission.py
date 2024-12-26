from rest_framework.permissions import BasePermission
from user.models import *
class DynamicPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        view_name = view.__class__.__name__   
        action = request.method.lower()
        if action=='post':
            action='add'
        if action in ['put', 'patch']:
            action="update" 
        user=CustomUser.objects.get(username=request.user)
        if user.rose=="manager":
            pass
            
        group=user.group
        for permission_groupe in group.permissions:
            permission = user.permission.filter(action=action, groupe=permission_groupe).first()
            if permission_groupe.view_name==view_name and permission.action==action:
                return True
        return False