from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

class Post(models.Model):
    """
    Model for user posts
    """
    title = models.CharField(
        max_length=200,
        verbose_name="Title",
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
    content = models.TextField(
        blank=True,
        null=True,
    )
    featured_image = CloudinaryField(
        'image', 
        default='placeholder'
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


    def save(self, *args, **kwargs):
            if not self.slug:
                # Generate a slug based on the username and post title
                base_slug = slugify(self.title)
                unique_slug = f"{base_slug}"  #not sure if User is correct variable here
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
    body = models.TextField()
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


