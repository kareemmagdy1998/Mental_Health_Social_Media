from django.contrib import admin
from .models import Person,Doctor

# Register your models here.
admin.site.register(Person)
admin.site.register(Doctor)