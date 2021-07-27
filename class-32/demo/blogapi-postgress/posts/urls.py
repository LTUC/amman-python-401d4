from django.urls import path

from .views import PostsListView, PostDetailsView

urlpatterns = [
    path('', PostsListView.as_view(), name='posts_api'), # /api/v1/posts/
    path('<int:pk>', PostDetailsView.as_view(), name='post_details_api'), # /api/v1/posts/<int:pk>
]
