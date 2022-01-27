from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    owner = models.BooleanField(null=False, default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']



class Room(models.Model):
    name = models.CharField(max_length=50 , null=True, unique=True)
    owner = models.ManyToManyField(User)    
    description = models.TextField(max_length=200, null=True)

    def __str__(self):
            return self.name
        

# one to many with Room 
class Issue(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=50 , blank=True, null=True)
    owner = models.ManyToManyField(User)

    description = models.TextField(max_length=300)
    isSolve = models.BooleanField(default=False)

    def __str__(self):
        return self.name

