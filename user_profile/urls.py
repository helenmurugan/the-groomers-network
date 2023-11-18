from . import views
from django.urls import path


urlpatterns = [
    path('update/<int:pk>/',views.ProfileUpdate.as_view(), name='my_profile_update'),
    path('<str:user>/',views.ProfileView.as_view(), name='my_profile'),
   
    # path('update/',views.ProfileUpdate.as_view(), name='my_profile_update'),
    # path('delete/',views.ProfileDelete.as_view(), name='profile_delete'),
    
]