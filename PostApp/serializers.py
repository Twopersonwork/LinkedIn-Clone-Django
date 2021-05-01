from rest_framework import serializers
from .models import Post, Like


# fields : includes fields from models which
# is to be shown in the response in API.
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'body', 'image', 'user']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'post', 'user']
