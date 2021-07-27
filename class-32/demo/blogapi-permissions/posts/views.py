from django.db import models
from django.shortcuts import render
from rest_framework import generics

from .models import Post
from .serializer import PostsSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class PostsListView(generics.ListCreateAPIView):    
    serializer_class = PostsSerializer
    queryset = Post.objects.all()

class PostDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostsSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)