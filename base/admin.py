from msilib.schema import Property
from django.contrib import admin
from .models import Address, User, Property


admin.site.register(User)
admin.site.register(Address)
admin.site.register(Property)
