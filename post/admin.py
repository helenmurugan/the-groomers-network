from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content', 'author']
    list_filter = ('created_on',)
    summernote_fields = ('content')



