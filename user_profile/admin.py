from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Customisation of profile in admin panel
    """
    list_display = ('user', 'full_name', 'company_name', 'location',)
    search_fields = ['full_name', 'company_name', 'location']
