from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Post(models.Model):
    """Model for the posts"""
    title = models.CharField(
        max_length=200,
        blank=False,
        null=True,
        verbose_name="post",
        help_text=(
            'format: required, unique=False'
        )
        )
    slug = models.SlugField(
        max_length=200, 
        unique=True
        )
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="post_posts"
    )
    updated_on = models.DateTimeField(
        auto_now=True
        )
    content = models.TextField()
    featured_image = CloudinaryField(
        'image', 
        default='placeholder'
        )
    excerpt = models.TextField(
        blank=True
        )
    created_on = models.DateTimeField(
        auto_now_add=True
        )
    likes = models.ManyToManyField(
        User, 
        related_name='post_likes', 
        blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


   


