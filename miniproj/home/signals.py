from .models import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from django.contrib.auth.signals import user_logged_in
from geopy.geocoders import Nominatim

@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        created=Driv_prof.objects.get_or_create(user=instance)

