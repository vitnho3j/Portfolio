from django.dispatch import receiver
from django.forms import ValidationError
from django import forms
from .models import Profile
from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import ProfileSocialMedia

def create_profile(sender, instance, created, **kwargs):
    if created:
        try:
            instance.profile
        except ObjectDoesNotExist:
            user_profile = Profile(user=instance)
            user_profile.save()


# @receiver(pre_save, sender=ProfileSocialMedia)
# def validate_social_media_limit(sender, instance, **kwargs):
#     profile = instance.profile
#     instance.clean_socials(profile)
#     profile = instance.profile
#     if profile and profile.medias.count() >= 6:
#         raise forms.ValidationError("Você atingiu o limite (6) de redes sociais que podem ser adicionadas, altere ou exclua uma rede social existente.")
