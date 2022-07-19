from django.db import models
from django.db.models import Model, CharField, TextField, DateTimeField, ForeignKey
from django.db.models import ManyToManyField, URLField, FloatField, IntegerField
# Create your models here.

class Articles(Model):
    published = CharField(max_length=15)
    name = CharField(max_length=50)
    url = URLField()


