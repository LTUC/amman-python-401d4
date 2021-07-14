from django.urls import path

from .views import HomeView, MoviesView, MovieDetailsView, MovieCreateView, MovieUpdateView, MovieDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('movies/', MoviesView.as_view(), name='movies'),
    path('movies/<int:pk>', MovieDetailsView.as_view(), name='movie_details'),
    path('movies/new', MovieCreateView.as_view(), name='movie_create'),
    path('movies/<int:pk>/update', MovieUpdateView.as_view(), name='movie_update'),
    path('movies/<int:pk>/delete', MovieDeleteView.as_view(), name='movie_delete')
]