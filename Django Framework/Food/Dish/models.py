from django.db import models

# Create your models here.
# class FoodItem(models:Model):
#     name = models.CharField(max_length=60)

class FoodItem(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    quantity=models.IntegerField()