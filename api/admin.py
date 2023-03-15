from django.contrib import admin
from .models import Item,Location

# ADDING ITEM AND LOCATION MODELS TO ADMIN PAGE
admin.site.register(Item)
admin.site.register(Location)
