from django.db import models
from django.db.models import Model, CharField, TextField, DateTimeField, ForeignKey
from django.db.models import ManyToManyField, URLField, FloatField, IntegerField
# Create your models here.

class Articles(Model):
    published = CharField(max_length=20)
    name = CharField(max_length=60)
    url = URLField()
    image=models.ImageField(upload_to='posts', null=True, blank=True)


