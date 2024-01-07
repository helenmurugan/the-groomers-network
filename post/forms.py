from .models import Post, Comment
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'tagline', 'content', 'featured_image',)
    
    content = forms.CharField



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    body = forms.CharField




        