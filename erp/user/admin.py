from django.contrib import admin
from .models import CustomUser, CustomGroup,  cordinates
admin.site.register(CustomUser)
admin.site.register(CustomGroup)
admin.site.register(cordinates)
# Register your models here.