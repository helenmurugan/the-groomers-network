from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content', 'author']
    list_filter = ('created_on',)
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    list_display = ('body', 'post', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('body',)




