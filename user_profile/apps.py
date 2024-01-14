from django.apps import AppConfig
from django.db.models.signals import post_save


class UserProfileConfig(AppConfig):
    """
    Configuration for user_profile app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_profile'

    def ready(self):
        from user_profile.signals import create_profile
        from django.contrib.auth.models import User
        post_save.connect(create_profile, sender=User)
        from user_profile.signals import save_profile
        post_save.connect(save_profile, sender=User)
