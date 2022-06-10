from email.policy import default
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Service(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class ServiceDetails(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    price = models.CharField(max_length=4)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="details")

    def __str__(self):
        return self.name



SERVICE_CHOICES =(
    ('PERFECT DAYS', 'Perfect Days'),
    ('ROYAL STONE', 'Royal Stone'),
    ('CLASSIC TREATMENT', 'Classic Treatment'),
    ('GROWTH FACTOR FACIAL','Growth Factor Facial'),
    ('VITAMIN C', 'Vitamin C'),
    ('DIAMOND BRIGHTENING FACIAL', 'Diamond Brightening Facial'),
    ('POWER GLO FACIAL', 'Power Glo Facial'),
    ('PINK HIMALAYAN SALT STONE MASSAGE', 'Pink Himalayan Salt Stone Massage'),
    ('PRENATAL MASSAGE', 'Prenatal Massage'),
    ('REFLEXOLOGY', 'Reflexology'),
    ('DEEP TISSUE MASSAGE', 'Deep Tissue Massage')

)
  
class Appointment(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    service = models.CharField(max_length=34, choices=SERVICE_CHOICES)
    email = models.CharField(max_length=150)
    number = models.CharField(max_length=15)
    date = models.DateField()
    time = models.CharField(max_length=9)

    def __str__(self):
        return self.fname, self.pk

     
class Review(models.Model):
    name = models.CharField(max_length=100)
    service = models.CharField(max_length=34, choices=SERVICE_CHOICES)
    rating = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(max_length=500)
    

    def __str__(self):
        return self.name
    class Meta:
        ordering=["-pk"]


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name