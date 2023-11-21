from .models import Post, Comment
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'featured_image',)
    
    content = forms.CharField(widget=SummernoteWidget)



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    body = forms.CharField(widget=SummernoteWidget)




        