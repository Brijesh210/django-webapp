from django.db.models import fields
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm


# from django.contrib.auth.models import User


class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['name', 'username', 'email',
                  'bio', 'groupId', 'residenceAddressId']


class IssueCreateForm(ModelForm):

    class Meta:
        model = Issue
        fields = '__all__'
        exclude = ['assigner', 'assignee', 'submitter']
        # ass exclude in view.py before save/commit


class IssueCategoryCreateForm(ModelForm):

    class Meta:
        model = IssueCategory
        fields = '__all__'


class CommentsCreateForm(ModelForm):

    class Meta:
        model = Comments
        fields = ['messageText']


class AddressCreateForm(ModelForm):

    class Meta:
        model = Address
        fields = '__all__'


class PropertyCreateForm(ModelForm):

    class Meta:
        model = Property
        fields = '__all__'
        exclude = ['ownerId']
        # add ownerId from view



class IssueUpdateForm(ModelForm):

    class Meta:
        model = Issue
        fields = ['assigner', 'assignee']
        # ass exclude in view.py before save/commit

