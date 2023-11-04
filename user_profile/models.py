from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    """Model for the User_profile"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='User',
        help_text=(
            'format: required, unique=True'
        )
    )
    first_name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='First name',
        help_text=(
            'format: not required, max_length=50'
        )
    )
    last_name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Last name',
        help_text=(
            'format: not required, max_length=50'
        )
    )
    avatar = CloudinaryField(
        'avatar',
        folder='avatars',
        blank=True,
        null=True,
    )
    company_name = models.TextField()
    company_logo = CloudinaryField(
        'image', 
        default='placeholder'
        )
    location = TextField(
        blank=True,
        null = True,
    )
    bio = TextField(
        blank=True,
        null = True,
    )

    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        if self.first_name:
            return self.first_name
        return self.user.username
