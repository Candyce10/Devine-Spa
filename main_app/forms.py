from django.forms import ModelForm


from .models import Review, Appointment


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['name','service', 'rating', 'comment']


