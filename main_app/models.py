from sys import maxsize
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Service(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    packagename1 = models.TextField(max_length=500)
    packageprice1 = models.TextField(max_length=500)
    packagename2 = models.TextField(max_length=500)
    packageprice2 = models.TextField(max_length=500)
    packagename3 = models.TextField(max_length=500)
    packageprice3 = models.TextField(max_length=500)

    def __str__(self):
        return self.name

   
  

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    number = models.CharField(max_length=15)
    date = models.CharField(max_length=10)

    def __str__(self):
        return self.name




SERVICE_CHOICES =(
    ('MASSAGE', 'massage'),
    ('FACIAL', 'facial'),
    ('PACKAGE', 'package'),
)
     
class Review(models.Model):
    name = models.CharField(max_length=100)
    service = models.CharField(max_length=7, choices=SERVICE_CHOICES, default='massage')
    rating = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(max_length=500)
    

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email