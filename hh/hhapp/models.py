from django.db import models
from django.db.models import Model, CharField, TextField, DateTimeField, ForeignKey
from django.db.models import ManyToManyField, URLField, FloatField, IntegerField
from usersapp.models import BlogUser
# Create your models here.



class Articles(Model):
    published = CharField(max_length=20)
    name = CharField(max_length=60)
    url = URLField()
    image=models.ImageField(upload_to='posts', null=True, blank=True)
    user=models.ForeignKey(BlogUser, on_delete=models.CASCADE)

    def has_image(self):
        print('my image: ', self.image)
        print('type', type(self.image))
        return bool(self.image)
    def some_method(self):
        return 'hello from method'
    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name='Post'
        verbose_name_plural = 'Posts'



class Tag(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=16, unique=True)
    description = models.TextField(blank=True)


