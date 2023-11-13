from . import views
from django.urls import path


urlpatterns = [
    path('/',views.ProfileView.as_view(), name='my_profile'),
]