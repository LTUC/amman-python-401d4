from django.db import models
from django.urls import reverse


# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=64)
    desc = models.TextField()
    director = models.CharField(max_length=64)
    watcher = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)
    rank = models.IntegerField(default=5)
    def __str__(self):
        return self.name
    # def get_absolute_url(self):
    #     return reverse('movies') # some url that shows you list of movie
    def get_absolute_url(self):
        return reverse('movie_details', args=[str(self.id)])


"""
Django Movie
With the help of a German bounty-hunter, a freed slave sets out to rescue his wife from a brutal plantation-owner in Mississippi.
Quentin Tarantino
Ahmad
"""