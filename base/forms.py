from django.forms import ModelForm
from .models import User
from django.contrib.auth.forms import UserCreationForm


# from django.contrib.auth.models import User

class MyUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'bio', 'owner']
