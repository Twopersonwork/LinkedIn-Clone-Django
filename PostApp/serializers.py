from rest_framework import serializers
from .models import Post, Like, Comment


# fields : includes fields from models which
# is to be shown in the response in API.
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'body', 'image', 'user','no_of_like','no_of_comment']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
