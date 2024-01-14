from .models import Profile
from django import forms


class ProfileForm(forms.ModelForm):
    """
    Customisation of profile form
    """
    class Meta:
        model = Profile
        fields = ('full_name', 'company_name', 'location', 'bio',)
