from . import views
from django.urls import path


urlpatterns = [
      path('events/', views.EventList.as_view(), name='event'),
      path('<slug:slug>/', views.EventDetail.as_view(), name='event_detail'),
      path('like/<slug:slug>', views.EventLike.as_view(), name='event_like'),
]
