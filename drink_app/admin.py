from django.contrib import admin
from .models import Drink

# Register your models here.
# here we register the different tables we want to show up in admin panel
admin.site.register(Drink)