from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser,  Group, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from clientInfo.models import store
from rest_framework.authtoken.models import Token
from django.db import models

class GroupePermission(models.Model):
    views=models.CharField(null=True, max_length=50)
    name=models.CharField(null=True, max_length=100)
class UserCustomPermission(models.Model):
    CHOICES = [
        ("get", "get"),
        ("add", "add"),     
        ("delete", "delete"),
        ("update", "update"),     
    ]
    groupe=models.ForeignKey(GroupePermission, on_delete=models.CASCADE,related_name="users_permissions",null=True)
    name=models.CharField(null=True, max_length=100)
    action=models.CharField(default="get",choices=CHOICES, max_length=50)

class CustomUser(User):
    permission=models.ManyToManyField(UserCustomPermission,null=True)
    EmployeeAt = models.ForeignKey('clientInfo.store', on_delete=models.CASCADE, related_name="mes_employees", null=True, blank=True)
    group = models.ForeignKey('CustomGroup', on_delete=models.SET_NULL, related_name="group_user", null=True, blank=True, default=None)
    role = models.CharField(max_length=100, null=True, blank=True, default='')
    entrepots_responsible = models.ForeignKey('inventory.Entrepot', on_delete=models.SET_NULL, related_name="responsables" ,default=None, null=True, blank=True)
    equipe_affiliated = models.ForeignKey('Equipe', on_delete=models.SET_NULL, related_name="mes_membres" ,default=None, null=True, blank=True)
    adresse_ip = models.GenericIPAddressField(default='127.0.0.1', blank=True, null=True)

class cordinates(models.Model):
    User = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="mycoordinates")  # Link the log entry to an author (user)
    latitude = models.CharField(max_length=250, default="", null=True, blank=True)
    longitude = models.CharField(max_length=250, default="", null=True, blank=True)
    
class Equipe(models.Model):
    label = models.CharField(max_length=250, default="", null=True, blank=True)
    store = models.ForeignKey('clientInfo.store', on_delete=models.CASCADE, related_name="mes_equipes", null=True, blank=True)
    date_created = models.DateTimeField()

class MyLogEntry(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="myacts")  # Link the log entry to an author (user)
    description = models.TextField()  # Store the description of the event or change
    timestamp = models.DateTimeField(auto_now_add=True)  # Record the timestamp when the log entry is created
    store =models.ForeignKey('clientInfo.store', on_delete=models.CASCADE, related_name="ma_tracabilte", null=True, blank=True)


    class Meta:
        ordering = ['-timestamp']  # Display log entries in descending order of timestamp
               
class CustomGroup(Group):
    label = models.CharField(max_length=100, unique=False)
    description = models.TextField(max_length=2500)
    store = models.ForeignKey('clientInfo.store', on_delete=models.CASCADE, related_name="mes_groupes", null=True, blank=True, default=None)
    permissions_groupe=models.ManyToManyField(GroupePermission,null=True)
    

