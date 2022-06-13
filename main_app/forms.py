from django.forms import ModelForm
from .models import Review
from django import forms

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name','service', 'rating', 'comment']
    

