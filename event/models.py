from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Event(models.Model):
    """Model for the events"""
    title = models.CharField(
            max_length=200,
            verbose_name="event",
            help_text=(
                'format: required, unique=False'
            ),
        )
    slug = models.SlugField(
        max_length=200, 
        unique=True
        )
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="event_events"
    )
    content = models.TextField(
        blank=True,
        null=True,
    )
    featured_image = CloudinaryField(
        'image',
        default='placeholder'
        )
    excerpt = models.TextField(
        blank=True,
        null=True, 
        max_length=200,
        )
    created_on = models.DateTimeField(
        auto_now_add=True
        )
    updated_on = models.DateTimeField(
        auto_now=True
        )
    location = models.TextField(
        blank=True,
        null=True, 
        max_length=30,
    )
    date = models.DateTimeField(
    )
    time = models.DateTimeField(
    )
    likes = models.ManyToManyField(
        User, 
        related_name='event_likes', 
        blank=True,
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


