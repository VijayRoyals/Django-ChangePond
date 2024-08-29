from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator 
from django.utils.text import slugify

class TagLine(models.Model):
    caption = models.CharField(max_length=100)

    def __str__(self):
        return self.caption
    

class VlogAuthor(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email_address = models.CharField(max_length=70)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class portfolio_detail(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    age=models.IntegerField(validators=[MinValueValidator(18) , MaxValueValidator(50)])
    city = models.CharField(max_length=100,null=True)
    content = models.CharField(max_length=200,null=True)
    read_more = models.CharField(max_length=1000,null=True)
    full_name = models.SlugField(default='',db_index=True,editable=False)
    event_date = models.DateField(null=True)  # For storing date only
    event_time = models.TimeField(null=True)  # For storing time only
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    img_title=models.CharField(max_length=50,null=True)
    img_url = models.ImageField(upload_to='images/', blank=True, null=True)
    author = models.ForeignKey(VlogAuthor,on_delete=models.CASCADE,null=True)
    tags = models.ManyToManyField(TagLine,null=True)

    def save(self, *args, **kwargs):
        self.full_name = slugify(f'{self.first_name} {self.last_name}')
        super().save(*args,**kwargs)


    def __str__(self):
        return f'{self.first_name}  {self.last_name}'
 
 
class Comment(models.Model):
    user_name = models.CharField(max_length=60)
    user_email = models.CharField(max_length=70)
    comment = models.TextField(max_length=1000)
    post = models.ForeignKey(portfolio_detail,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.user_name