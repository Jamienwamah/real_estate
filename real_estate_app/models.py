from django.db import models


# Create your models here.
class listing(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.CharField(max_length=200)