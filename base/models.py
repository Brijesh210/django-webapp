from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    is_owner = models.BooleanField(default=False)
    is_tenant = models.BooleanField(default= False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.name


class Tenant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user


class Room(models.Model):
    name = models.CharField(max_length=50, null=True, unique=True)
    address = models.TextField(max_length=200, null= True)

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    tenant = models.OneToOneField(Tenant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# one to many with Room
class Issue(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=300)
    isSolve = models.BooleanField(default=False)

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
