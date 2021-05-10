from django.db import models

# Create your models here.


class reservation(models.Model):
    address = models.CharField(max_length=100)
    startdate = models.DateField() 
    username = models.CharField(max_length=50)
    noofpets = models.IntegerField()
    noofdays = models.IntegerField()
    email = models.EmailField(max_length=70,blank=True)
    phone = models.CharField(max_length=12)

class reservation2(models.Model):
    address = models.CharField(max_length=100)
    startdate = models.DateField() 
    username = models.CharField(max_length=50)
    noofpets = models.IntegerField()
    noofdays = models.IntegerField()
    email = models.EmailField(max_length=70,blank=True)
    phone = models.CharField(max_length=12)