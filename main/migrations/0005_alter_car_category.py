# Generated by Django 5.1 on 2024-08-22 15:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_category_car_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.category'),
        ),
    ]
