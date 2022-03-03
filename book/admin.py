"""
Admin.py file is used for registering the Django models into the Django administration.
It is used to display the Django model in the Django admin panel. It performs three major tasks:

a. Registering models
b. Creating a Superuser
c. Logging in and using the web application
"""

from book.models import Attraction, Location
from django.contrib import admin
from .models import Profile, Location, Attraction, Booking

# Register your models here.
admin.site.register(Location)
admin.site.register(Attraction)
admin.site.register(Profile)
admin.site.register(Booking)
