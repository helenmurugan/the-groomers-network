from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from user_profile.models import Profile
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)       


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


# @receiver(post_delete, sender=User)
# def logout (sender, instance, **kwargs):
#     if deleted:

