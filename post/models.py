from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify
from django.utils import timezone


class Post(models.Model):
    """
    Model for user posts
    """
    title = models.CharField(
        max_length=40,
        verbose_name="Title",
        )
    slug = models.SlugField(
        max_length=40,
        unique=True
        )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="post_posts"
    )
    content = models.TextField(
        blank=False,
        null=False,
        max_length=20000,
    )
    featured_image = CloudinaryField(
        'image',
        default='placeholder',
        blank=True,
        null=True,
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
    likes = models.ManyToManyField(
        User,
        related_name='post_likes',
        blank=True,
        )

    # following code on slug generation taken from Kim Bergstroem's PP4
    # https://github.com/KimBergstroem/PP4
    def save(self, *args, **kwargs):
        """
        Generate a slug based on post title and timestamp and save
        """
        if not self.slug:
            base_slug = slugify(self.title)
            timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
            unique_slug = f"{base_slug}-{timestamp}"
            self.slug = unique_slug

        return super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Model for comments
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
        )
    name = models.CharField(
        blank=True,
        null=True,
        max_length=80
        )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="post_comment"
        )
    body = models.TextField(
        max_length=1000,
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_on"]

        def __str__(self):
            """
            Returns string for comment
            """
            return f"Comment {self.body} by {self.name}"
