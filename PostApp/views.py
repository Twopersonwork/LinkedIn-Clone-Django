from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from .models import Post,Like
from .serializers import PostSerializer,LikeSerializer
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

# to create the post
@api_view(['POST'])
def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# queryset : set of all post objects
# serializer_class : present them in a way mentioned in serializers.py
class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


    # this will create the object in Like table for
    # respective post and user,who has liked the post.
    @action(detail=True, methods=['POST'])
    def likePost(self, request, pk=None):
        post = Post.objects.get(id=pk)
        user = request.user
        likes = Like.objects.create(user=user, post=post)
        serializer = LikeSerializer(likes, many=False)
        response = {'message': 'Liked Post', 'result': serializer.data}
        return Response(response, status=status.HTTP_200_OK)


    # this will delete the object in Like table for
    # respective post and user,who has disliked the post.
    @action(detail=True, methods=['DELETE'])
    def dislikePost(self, request, pk=None):
        post = Post.objects.get(id=pk)
        user = request.user
        likes = Like.objects.get(user=user.id, post=post.id)
        likes.delete()
        response = {'message': 'Disliked Post so deleted'}
        return Response(response,status=status.HTTP_204_NO_CONTENT)







# queryset : set of all like objects
# serializer_class : present them in a way mentioned in serializers.py
class LikeViewset(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer