from django.db import models

from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title