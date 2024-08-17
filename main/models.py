from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='images/')


class Car(models.Model):
    name = models.CharField(max_length=300)
    produced_year = models.DateField()
    color = models.CharField(max_length=200)
    images = models.ForeignKey(Image, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    case = models.CharField(max_length=200)
    location = models.CharField(max_length=500)

class Account(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()

