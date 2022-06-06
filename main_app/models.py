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
  
  v