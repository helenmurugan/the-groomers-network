from . import views
from django.urls import path


urlpatterns = [
    path('<str:user>/',views.ProfileView.as_view(), name='my_profile'),
]