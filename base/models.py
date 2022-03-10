from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserGroup(models.Model):
    groupName = models.CharField(max_length=50, null=True)

    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.groupName


class Address(models.Model):
    street = models.CharField(max_length=20, null=True)
    apartment =models.IntegerField(null=True)
    city = models.CharField(max_length=10, null=True)
    zipCode = models.IntegerField(null=True)
    country = models.CharField(max_length=10, null=True)  

    def __str__(self) -> str:
        return self.street + str(self.apartment)


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    groupId = models.ForeignKey(UserGroup, on_delete=models.CASCADE, null=True)
    residenceAddressId = models.ForeignKey(Address, on_delete=models.CASCADE, null=True) 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    

class Property(models.Model):
    name = models.CharField(max_length=50, null=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)
    ownerId = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner_property_set")
    tenants = models.ManyToManyField(User, related_name="tenant_property_set")

    def __str__(self) -> str:
        return self.name



class IssueCategory(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title


class Issue(models.Model):
    class StatusENUM(models.TextChoices):
        CREATED = 'CRE',
        ASSIGED = 'ASS'
        PROGRESS = 'PRO'
        COMPLATED = 'COM'
        DELETED = 'DEL'
        CLOSED = 'CLO'

    name = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=200, null=True)

    category = models.ForeignKey(IssueCategory, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Property, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=StatusENUM.choices, default=StatusENUM.CREATED)

    assigner = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name="assigned_by_issues_set")
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name="assigned_to_issues_set")
    submitter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="submitted_issues_set")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['-updated', '-created']
        


class Comments(models.Model):
    messageText = models.TextField(max_length=200, null=True)

    authorId = models.ForeignKey(User, on_delete=models.CASCADE)
    issueId = models.ForeignKey(Issue, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']

