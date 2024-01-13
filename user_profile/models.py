from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    """
    Model for the user profiles
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='User',
    )
    full_name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Full name',
        default='',
    )
    company_name = models.CharField(
        blank=True,
        null=True,
        max_length=30,
        default='',
    )
    location = models.CharField(
        blank=True,
        null=True,
        max_length=30,
        default='',
    )

    bio = models.TextField(
        blank=True,
        null=True,
        max_length=1000,
        default='',
    )
