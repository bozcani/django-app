from django.contrib import admin

from .models import Person, Trip, Traveler
# Register your models here.
admin.site.register(Person)
admin.site.register(Trip)
admin.site.register(Traveler)