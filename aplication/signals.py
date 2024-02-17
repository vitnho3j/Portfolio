from .models import Profile
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

def create_profile(sender, instance, created, **kwargs):
    if created:
        try:
            instance.profile
        except ObjectDoesNotExist:
            user_profile = Profile(user=instance)
            user_profile.save()

post_save.connect(create_profile, sender=User)
