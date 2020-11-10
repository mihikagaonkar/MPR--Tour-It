from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Customer)
admin.site.register(Place)
admin.site.register(PlaceType)
admin.site.register(Itinerary)
