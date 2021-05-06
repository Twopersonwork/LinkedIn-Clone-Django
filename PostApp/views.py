from rest_framework import viewsets
from .models import Post, Like, Comment
from .serializers import PostSerializer, LikeSerializer, CommentSerializer
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import datetime


# to create the post
@api_view(['POST'])
def create_post(request):
    request.data._mutable = True
    request.data['user'] = request.user.id
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# queryset : set of all post objects
# serializer_class : present them in a way mentioned in serializers.py
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    # this will create the object in Like table for
    # respective post and user,who has liked the post.
    @action(detail=True, methods=['POST'])
    def likePost(self, request, pk=None):
        post = Post.objects.get(id=pk)
        user = request.user
        try:
            likes = Like.objects.create(user=user, post=post)
        except:
            return Response({'message': 'You have already liked the post'})
        serializer = LikeSerializer(likes, many=False)
        response = {'message': 'Liked Post', 'result': serializer.data}
        return Response(response, status=status.HTTP_200_OK)


    # this will delete the object in Like table for
    # respective post and user,who has disliked the post.
    @action(detail=True, methods=['DELETE'])
    def dislikePost(self, request, pk=None):
        post = Post.objects.get(id=pk)
        user = request.user
        try:
            likes = Like.objects.get(user=user, post=post)
            likes.delete()
        except Exception:
            return Response({'message': "You haven't liked the post yet."})
        response = {'message': 'Disliked Post so deleted'}
        return Response(response, status=status.HTTP_204_NO_CONTENT)


    @action(detail=True, methods=['POST'])
    def comment(self, request, pk=None):
        post = Post.objects.get(id=pk)
        user = request.user
        comment = Comment.objects.create(user=user, post=post, comment=request.data['comment'])
        serializer = CommentSerializer(comment, many=False)
        response = {'message': 'commented on the Post', 'result': serializer.data}
        return Response(response, status=status.HTTP_200_OK)


    @action(detail=True, methods=['DELETE'])
    def uncomment(self, request, pk=None):
        post = Post.objects.get(id=pk)
        # user = User.objects.get(id=request.data['user'])
        user = request.user
        try:
            comment = Comment.objects.get(user=user, post=post)
            comment.delete()
        except Exception:
            return Response({'message': "You haven't comment on the post yet."})
        response = {'message': 'comment deleted'}
        return Response(response, status=status.HTTP_204_NO_CONTENT)


# queryset : set of all like objects
# serializer_class : present them in a way mentioned in serializers.py
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    http_method_names = ['get','delete']
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['DELETE'])
    def uncomment(self, request, pk=None):
        # comment = Comment.objects.get(id=pk)
        # user = User.objects.get(id=request.data['user'])
        # user = request.user
        try:
            comment = Comment.objects.get(pk=pk)
            comment.delete()
        except Exception:
            return Response({'message': "You haven't comment on the post yet."})
        response = {'message': 'comment deleted'}
        return Response(response, status=status.HTTP_204_NO_CONTENT)
