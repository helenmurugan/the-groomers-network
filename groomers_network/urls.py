from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('posts/', include('post.urls'), name='post_urls'),
    path('events/', include('event.urls'), name='event_urls'),
    path('accounts/', include('allauth.urls')),
    path('', include('pages.urls'), name='landing_page'),
    path('user_profile/', include('user_profile.urls')),
]
