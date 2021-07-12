from django.urls import path

from .views import HomeView, MoviesView, MovieDetailsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('movies/', MoviesView.as_view(), name='movies'),
    path('movies/<int:pk>', MovieDetailsView.as_view(), name='movie_details'),
]