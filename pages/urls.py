from . import views
from django.urls import path


urlpatterns = [
      path(
            '',
            views.landing_page,
            name='landing_page'
      ),
      path(
            '403/',
            views.Error403,
            name='error403'
      ),
      path(
            '404/',
            views.Error404,
            name='error404'
      ),
      path(
            '405/',
            views.Error405,
            name='error405'
      ),
      path(
            '500/',
            views.Error500,
            name='error500'
      ),

]
