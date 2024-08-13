from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Author(models.Model):
    First_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100,null=True)
    rating = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(2)], null=True)

    def __str__(self):
        return f"{self.First_name}  {self.last_name}"

    