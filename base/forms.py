from django.db.models import fields
from django.forms import ModelForm
from .models import User, Room, Issue
from django.contrib.auth.forms import UserCreationForm


# from django.contrib.auth.models import User

class MyUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'bio', 'owner']

class RoomForm(ModelForm):

    class Meta:
        model = Room
        fields = [ 'name', 'description' ]

class IssueForm(ModelForm):

    class Meta:
        model = Issue
        fields = [ 'owner', 'room', 'name', 'description' ]



class TenantForm(ModelForm):

    class Meta:
        model = Issue
        fields = [ 'room','name', 'description' ]