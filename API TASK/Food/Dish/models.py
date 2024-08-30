from django.db import models
from Category.models import CategoryModel
# Create your models here.



def dishImagePath(instance, filename):
    return '/'.join(['uploads', str(instance.dishName), filename])


class DishModel(models.Model):
    dishName = models.CharField(max_length=100)
    price = models.IntegerField()
    dishImage = models.ImageField(upload_to=dishImagePath,null=True,blank=True)
    categoryId = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.dishName