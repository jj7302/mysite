from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from mysite import settings
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.CharField(max_length=60, blank=True)
    organization_key = models.CharField(max_length=60, blank=True)
    access = models.CharField(max_length=30, blank=True)


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user.username



class Voulunteer_Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=200)
    hours = models.DecimalField(max_digits=3, decimal_places=1)
    date = models.DateTimeField("date published", default=timezone.now())

    def __str__(self):
        return self.event_name

class Planned_Event(models.Model):
    event_name = models.CharField(max_length=200)
    hours = models.DecimalField(max_digits=3, decimal_places=1)
    date = models.DateTimeField("date published", default=timezone.now())

    def __str__(self):
        return self.event_name



