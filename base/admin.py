from django.contrib import admin
from .models import User, Issue, Room
# Register your models here.
admin.site.register(User)
admin.site.register(Room)
admin.site.register(Issue)