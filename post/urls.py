from . import views
from django.urls import path


urlpatterns = [
      path("", views.PostList.as_view(), name="home"),
      path(
            "posts/post_create/",
            views.PostCreate.as_view(),
            name="post_create"
      ),
      path(
            "posts/update/<slug:slug>",
            views.PostUpdate.as_view(),
            name="post_update"
      ),
      path(
            "posts/delete/<slug:slug>",
            views.PostDelete.as_view(),
            name="post_confirm_delete"
      ),
      path(
            "comment/delete/<int:pk>/",
            views.CommentDelete.as_view(),
            name="comment_confirm_delete"
      ),
      path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
      path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
