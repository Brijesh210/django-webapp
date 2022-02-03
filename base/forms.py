from django.db.models import fields
from django.forms import ModelForm
from .models import User, Room, Issue
from django.contrib.auth.forms import UserCreationForm


# from django.contrib.auth.models import User

class OwnerForm(UserCreationForm):
    
    class Meta:
        model = User
        model.is_owner = True
        
        fields = ['name', 'username', 'email', 'bio',]



class TenantForm(UserCreationForm):
    
    class Meta:
        model = User
        model.is_tenant = True
        fields = ['name', 'username', 'email', 'bio',]


class RoomForm(ModelForm):

    class Meta:
        model = Room
        fields = [ 'name', 'address' ]


class IssueForm(ModelForm):
    
    class Meta:
        model = Issue
        fields = [ 'owner', 'room', 'name', 'description' ]
