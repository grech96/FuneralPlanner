from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    birthday = models.DateField()
    phone = models.IntegerField (null= False)
    city = models.CharField(max_length=100, null = True)
    
class Responsable(models.Model):
    name = models.CharField(max_length=200, null = True)
    birthday = models.DateField()
    phone = models.IntegerField (null= False)
    email = models.EmailField (null = False)

class Planner(models.Model):
    ashes = models.CharField(max_length=200, null = True)
    venue = models.TextField(max_length=200, null = True)
    wish = models.TextField(max_length=600, null = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class NoGuest(models.Model):
    name = models.CharField(max_length=200, null = True)
    Planner = models.ForeignKey(Planner, on_delete=models.CASCADE)

class FuneralService(models.Model):
    name = models.CharField(max_length=100, null = True)
    description = models.TextField(max_length=500, null = True)
    planner = models.ManyToManyField(User)


class Additional(models.Model):
    name = models.CharField(max_length=100, null = True)
    description = models.TextField(max_length=500, null = True)