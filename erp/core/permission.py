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
        permission = user.permission.filter(action=action, view=view_name).first()
        if permission:
                return True
        return False