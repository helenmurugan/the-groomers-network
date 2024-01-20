from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Event(models.Model):
    """
    Model for an event
    """
    title = models.CharField(
            max_length=40,
            verbose_name="event",
        )
    slug = models.SlugField(
        max_length=40,
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
        max_length=5000,
    )
    featured_image = CloudinaryField(
        'image',
        default='placeholder'
        )
    tagline = models.CharField(
        max_length=40,
        null=True,
        blank=True,
    )
    created_on = models.DateTimeField(
        auto_now_add=True
        )
    updated_on = models.DateTimeField(
        auto_now=True
        )
    location = models.CharField(
        blank=True,
        null=True,
        max_length=40,
    )
    date_time = models.DateTimeField(
        verbose_name='Date and Time'
    )
    likes = models.ManyToManyField(
        User,
        related_name='event_likes',
        blank=True,
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        """
        Returns string for event title/name
        """
        return self.title

    def number_of_likes(self):
        """
        Returns number of likes
        """
        return self.likes.count()
