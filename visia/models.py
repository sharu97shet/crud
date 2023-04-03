from django.db import models

# Create your models here.


class Service(models.Model):
    # id=models.CharField(max_length=200)

    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics', default="")
    desc = models.TextField(max_length=250)
    # price=models.IntegerField(default='333')

    # id:int
    # name:str
    # img:str
    # desc:str
    # price:int


class Contact(models.Model):

    Name = models.CharField(max_length=250)
    EmailID = models.EmailField(max_length=254)
    Address = models.TextField(max_length=200)
    Qualification = models.TextField(max_length=200)
    Experience = models.TextField(max_length=200)
