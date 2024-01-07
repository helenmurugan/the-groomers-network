from .models import Post, Comment
from django import forms
from crispy_forms.helper import FormHelper


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'tagline', 'content', 'featured_image',)
    
   
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {'body': '',}

  




        