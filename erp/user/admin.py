from django.contrib import admin
from .models import CustomUser, CustomGroup,  cordinates,UserCustomPermission
admin.site.register(CustomUser)
admin.site.register(CustomGroup)
admin.site.register(cordinates)
admin.site.register(UserCustomPermission)


# Register your models here.