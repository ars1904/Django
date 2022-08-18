from django.db import models
from django.db.models import Model, CharField, TextField, DateTimeField, ForeignKey
from django.db.models import ManyToManyField, URLField, FloatField, IntegerField
from usersapp.models import BlogUser
# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=16, unique=True)
    description = models.TextField(blank=True)



class ActiveManager(models.Manager):
    def get_queryset(self):
        all_objects=super().get_queryset()
        return all_objects.filter(is_active=True)

class IsActiveMixin(models.Model):
    objects = models.Manager()
    active_objects = ActiveManager()
    is_active = models.BooleanField(default=False)

    class Meta:
        abstract = True

class Tag(IsActiveMixin):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name

class Articles(IsActiveMixin):
    objects=models.Manager()
    active_objects=ActiveManager()
    published = CharField(max_length=20)
    name = CharField(max_length=60)
    url = URLField()
    image=models.ImageField(upload_to='posts', null=True, blank=True)
    user=models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    rating=models.PositiveSmallIntegerField(default=1)
    is_active=models.BooleanField(default=False)

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







