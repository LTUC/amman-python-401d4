from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Movie

class HomeView(TemplateView):
    template_name = 'home.html'

class MoviesView(ListView):
    template_name = 'movies.html'
    model = Movie

class MovieDetailsView(DetailView):
    template_name = 'movie_details.html'
    model = Movie

class MovieCreateView(CreateView):
    template_name = 'movie_create.html'
    model = Movie
    fields = ['name', 'desc', 'director', 'watcher','rank']

class MovieUpdateView(UpdateView):
    template_name = 'movie_update.html'
    model = Movie
    fields = ['name', 'desc', 'director', 'watcher', 'rank']

class MovieDeleteView(DeleteView):
    template_name = 'movie_delete.html'
    model = Movie
    success_url = reverse_lazy('movies')