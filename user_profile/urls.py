from . import views
from django.urls import path


urlpatterns = [
    path('<str:user>/', views.ProfileView.as_view(), name='my_profile'),
    path('update/<int:pk>/', views.ProfileUpdate.as_view(), name='my_profile_update'),
]
   
  
