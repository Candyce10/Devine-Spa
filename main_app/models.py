from django.db import models

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

    class Meta:
        ordering = ['name']
  
class Review(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField(default=5)
    comment = models.TextField(max_length=500)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return self.name

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    number = models.CharField(max_length=15)

    def __str__(self):
        return self.name