from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator 
from django.utils.text import slugify

# Create your models here.

class author(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    age=models.IntegerField(validators=[MinValueValidator(18) , MaxValueValidator(50)])
    city = models.CharField(max_length=100,null=True)
    rating = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(2)],null= True)
    full_name = models.CharField(max_length=20,null=True,editable=False)
    slug = models.SlugField(default='',db_index=True,editable=False)


    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.first_name} {self.last_name} {self.rating}')
        self.full_name = slugify(f'{self.first_name} {self.last_name}')
        super().save(*args,**kwargs)


    def __str__(self):
        return f'Author Details : -->   Full Name :  {self.first_name}  {self.last_name} ,  AGE : {self.age}  , City : {self.city} , Rating : {self.rating}'
 
 