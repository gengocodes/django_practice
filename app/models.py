from django.db import models

# Create your models here.
class Menuitems(models.Model):
    name = models.CharField(max_length=200)
    course = models.CharField(max_length=300)
    year = models.IntegerField()

class Drinks(models.Model):
    drink_name = models.CharField(max_length=200)
    price = models.IntegerField()
