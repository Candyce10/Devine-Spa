from django.forms import ModelForm
from d

from .models import Review, Appointment


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['name','service', 'rating', 'comment']

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['name','service', 'email', 'number', 'date']


