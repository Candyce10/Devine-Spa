from django.contrib import admin
from .models import Service, Review, Appointment, Contact, ServiceDetails

admin.site.register(Service)
admin.site.register(ServiceDetails)
admin.site.register(Review)
admin.site.register(Appointment)
admin.site.register(Contact)