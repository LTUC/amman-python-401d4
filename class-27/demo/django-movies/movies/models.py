from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=64)
    desc = models.TextField()
    director = models.CharField(max_length=64)
    watcher = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)
    rank = models.IntegerField(default=10)
    def __str__(self):
        return self.name


"""
Django Movie
With the help of a German bounty-hunter, a freed slave sets out to rescue his wife from a brutal plantation-owner in Mississippi.
Quentin Tarantino
Ahmad
"""