from django.views.generic import TemplateView, ListView, DetailView

from .models import Movie

class HomeView(TemplateView):
    template_name = 'home.html'

class MoviesView(ListView):
    template_name = 'movies.html'
    model = Movie

class MovieDetailsView(DetailView):
    template_name = 'movie_details.html'
    model = Movie