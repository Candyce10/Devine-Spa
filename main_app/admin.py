from django.contrib import admin
from .models import Service, Review, Appointment

admin.site.register(Service)
admin.site.register(Review)
admin.site.register(Appointment)