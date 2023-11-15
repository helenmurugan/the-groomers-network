from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from .models import Profile


class ProfileView(View):
    """
    View for the profile page.
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
 
