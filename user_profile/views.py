from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.views.generic import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Profile
from .forms import ProfileForm 

class ProfileView(View):
    """
    View for reading the profile page.
    """
    def get(self, request, *args, **kwargs):
        """
        Get the profile page
        """
        if request.user.is_authenticated:
            user_profile = get_object_or_404(
                Profile,
                user=request.user
            )
            print(user_profile)
            context = {
                'user_profile': user_profile,
            }
            return render(
                request,
                'my_profile.html',
                context
            )
        else:
            return render(
                request,
                'account/login.html'
            )


class ProfileUpdate(SuccessMessageMixin, UpdateView):
    """
    View for updating a profile

    """
    model = Profile
    form_class = ProfileForm
    template_name = "my_profile_update.html"
    success_url ="/user_profile/<str:user>"
    success_message = "Your profile has been updated!"















    
