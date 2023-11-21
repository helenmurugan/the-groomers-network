from .models import Profile
from django import forms
from django_summernote.widgets import SummernoteWidget



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('full_name', 'company_name', 'location', 'bio',)

    bio = forms.CharField(widget=SummernoteWidget)