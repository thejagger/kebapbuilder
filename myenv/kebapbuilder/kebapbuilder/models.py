from django.db import models

from django.contrib import admin

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)

    def __str__(self):
        return self.firstname + ' ' + self.lastname

class Additional(models.Model):
    additional_name = models.CharField(max_length=70)
    additional_price = models.FloatField(default=0)

    def __str__(self):
        return f'{self.additional_name} ({self.additional_price}€)'

class MainType(models.Model):
    main_type_name = models.CharField(max_length=70)
    main_type_price = models.FloatField(default=0)

    def __str__(self):
        return f'{self.main_type_name} ({self.main_type_price}€)'

class Type(models.Model):
    type_name = models.CharField(max_length=70)
    type_price = models.FloatField(default=0)

    def __str__(self):
        return f'{self.type_name} ({self.type_price}€)'

class Order(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    main_type = models.ForeignKey(MainType, on_delete=models.CASCADE)
    additionals = models.ManyToManyField(Additional)
    is_ordered = models.BooleanField(default=False)
    order_date = models.DateField(default=None, blank=True)