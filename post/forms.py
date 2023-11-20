from .models import Post, Comment
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'featured_image',)

    # widgets = {
    #         "category": forms.Select(attrs={"class": "form-control"}),
    #         "device": forms.Select(attrs={"class": "form-control"}),
    #         "content": SummernoteWidget(attrs={"class": "form-control"}),
    #         "title": forms.TextInput(
    #             attrs={"class": "form-control",
    #                    "placeholder": "Max 50 characters"}
    #         ),
    #         "excerpt": forms.TextInput(
    #             attrs={"class": "form-control",
    #                    "placeholder": "Max 75 characters"}
    #         ),
    #     }

    #make sense of this to get the wysiwyg editor working



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)




        