from django.db import models



class CarBrand(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    logo = models.ImageField(upload_to='logo', blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class CarColor(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=300,  blank=True, null=True)
    produced_year = models.DateField(blank=True, null=True)
    color = models.ForeignKey(CarColor, on_delete=models.CASCADE, related_name='color', blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    case = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=500, blank=True, null=True)
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='cars', blank=True, null=True)
    fuel = models.CharField(max_length=500, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='images', blank=True, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, blank=True, null=True)

  