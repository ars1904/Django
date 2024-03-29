from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class BlogUser(AbstractUser):
    email=models.EmailField(unique=True)
    is_author=models.BooleanField(default=False)

    def save(self,*args,**kwargs):
        user=super().save(*args,**kwargs)
        if not Profile.objects.filter(user=self).exists():
            Profile.objects.create(user=self)

class Profile(models.Model):
    info=models.TextField(blank=True)
    user=models.OneToOneField(BlogUser, on_delete=models.CASCADE,null=True, blank=True)

#@receiver(post_save, sender=BlogUser)
#def create_profile(sender, instance, **kwargs):
    #print('Сработал обработчик сигнала')
    #if not Profile.objects.filter(user=instance).exists():
        #Profile.objects.create(user=instance)