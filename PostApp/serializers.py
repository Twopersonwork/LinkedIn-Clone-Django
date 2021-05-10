from rest_framework import serializers
from .models import Post, Like, Comment


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = "__all__"



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


# fields : includes fields from models which
# is to be shown in the response in API.
class PostSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(read_only=True, many=True)
    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ['id', 'body', 'image', 'user', 'likes', 'comments', 'no_of_like', 'no_of_comment']

    # def get_likes(self, obj):
    #     return LikesSerializer(obj.user.all(), many=True).data
    #
    #
    # def get_comments(self, obj):
    #     return CommentsSerializer(obj.comments.all(), many=True).data

# class LikesSerializer(serializers.ModelSerializer):
#     username = serializers.ReadOnlyField(source='user.username') # to get the username of following_user_id
#     user = UserSerializer(many=True)
#     class Meta:
#         model = Like
#         fields = ['id','user']
#
# class CommentsSerializer(serializers.ModelSerializer):
#     username = serializers.ReadOnlyField(source='user.username')  # to get the username of following_user_id
#     class Meta:
#         model = Comment
#         fields = ['id','username']
