from rest_framework import serializers

from .models import Post

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'body', 'created_at', 'author')
        model = Post