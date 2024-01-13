from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.views.generic import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.models import User


class ProfileView(View):
    """
    View for retrieving data and viewing my_profile page.
    """
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user_profile = get_object_or_404(
                Profile,
                user=request.user
            )
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
    View for updating my_profile

    """
    model = Profile
    form_class = ProfileForm
    template_name = "my_profile_update.html"
    success_url = "/user_profile/<str:user>"
    success_message = "Your profile has been updated!"


def get_user_profile(request, username):
    """
    View for retrieving data and viewing a user's profile
    """
    user = User.objects.get(username=username)
    user_profile = get_object_or_404(Profile, user=user)
    return render(
        request,
        'user_profile.html',
        {"user_profile": user_profile}
    )
