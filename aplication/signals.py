from django.dispatch import receiver
from .models import Profile
from django.db.models.signals import post_save
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
        # profile = Profile.objects.get(user=instance)
        # profile.description = "Insira sua descrição aqui! (Delete o texto atual)"
        # profile.save()

post_save.connect(create_profile, sender=User)
