from . import views
from django.urls import path


urlpatterns = [
      path(
            '',
            views.landing_page,
            name='landing_page'
      ),
      path(
            '404/',
            views.Error404,
            name='error404'
      ),
]
