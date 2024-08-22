from django.contrib import admin

from main.models import Car, CarBrand, CarColor, Category, Image



admin.site.register(Image)
admin.site.register(Car)
admin.site.register(CarColor)
admin.site.register(CarBrand)
admin.site.register(Category)
