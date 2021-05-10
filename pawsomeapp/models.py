from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager ,UserManager, PermissionsMixin

# Create your models here.

class Pets(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    colour = models.CharField(max_length=100)
    offer = models.TextField()
    location = models.TextField()


class pList(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    breed = models.CharField(max_length=100)
    offer = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    petbreedername = models.CharField(max_length=100)
    petbreederimg = models.ImageField(upload_to='pics', default="")
    petbreederphone = models.CharField(max_length=12, default="")
    petbreederemail = models.CharField(max_length=30, default="")
    petbreederoffer = models.CharField(max_length=200)
    petbreederlocation = models.CharField(max_length=100, default="")
    petbreederstatus = models.CharField(max_length=100)

class ppList(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    brand = models.CharField(max_length=100)
    offer = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.CharField(max_length=100)


class daycare(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    location = models.CharField(max_length=100)
    adds = models.CharField(max_length=100)
    price = models.IntegerField()
    phone = models.IntegerField()


class caretaker(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=30, default="")
    password = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    location = models.CharField(max_length=100)
    adds = models.CharField(max_length=100)
    rate = models.IntegerField()
    contact = models.CharField(max_length=12, default="")
    experience = models.IntegerField()
    objects =  UserManager()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)


class vet(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    phone = models.CharField(max_length=12, default="")
    email = models.CharField(max_length=30, default="")
    location = models.CharField(max_length=100, default="")
    status = models.CharField(max_length=100)


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name


class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    amount=models.IntegerField(default=0)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")


class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."


class ContactForm(models.Model):
    from_email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=70)
    message = models.CharField(max_length=5000)    # error may occur
    to_email = models.EmailField(max_length=254)