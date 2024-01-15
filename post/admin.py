from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Customisation of post in admin panel
    """
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'tagline', 'created_on')
    search_fields = ['title', 'content', 'tagline', 'author__username']
    list_filter = ('created_on',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Customisation of comments in admin panel
    """
    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('created_on',)
    search_fields = ['name', 'body']
