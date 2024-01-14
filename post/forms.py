from .models import Post, Comment
from django import forms
from crispy_forms.helper import FormHelper


class PostForm(forms.ModelForm):
    """
    Customisation of form to create or update a post
    """
    class Meta:
        model = Post
        fields = ('title', 'tagline', 'content', 'featured_image',)


class CommentForm(forms.ModelForm):
    """
    Customisation of form to create a comment
    """
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {'body': 'Leave a comment', }
