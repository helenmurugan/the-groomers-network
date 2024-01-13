from django.contrib import admin
from .models import Event
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'tagline', 'location', 'date_time', 'created_on')
    list_filter = ('created_on',)
    search_fields = ['title', 'content', 'location', 'tagline']
    summernote_fields = ('content')
