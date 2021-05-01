from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import UserSerializer, UserFollowingSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import UserFollowing


# First get the all the users and then display in a way mentioned in UserSerializers.
class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# To see following and followers of all the users.
class UserFollowingViewSet(viewsets.ModelViewSet):
    queryset = UserFollowing.objects.all()
    serializer_class = UserFollowingSerializer
    http_method_names = ['get']


# For follow and Unfollow
class UserFollow(APIView):
    # return user if user exist
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise ValueError

    # get the users follow details.
    def get(self, request, pk, format=None):
        try:
            user = self.get_object(pk)
        except Exception:
            return Response({'message': 'User does not exists '})
        serializer = UserSerializer(user)
        return Response(serializer.data)

    # follow another users
    def post(self, request, pk, format=None):
        user = User.objects.get(pk=request.data['user'])
        try:
            follow = self.get_object(pk)
        except Exception:
            return Response({'message': 'User does not exists '})
        try:
            UserFollowing.objects.create(user_id=user, following_user_id=follow)
        except Exception as e:
            return Response({"message": f"You already follow {follow}"})

        # serializer = UserSerializer(follow)
        return Response({'message': f'You follow {follow}'})

    # unfollow users.
    def delete(self, request, pk, format=None):
        user = User.objects.get(pk=request.data['user'])
        try:
            follow = self.get_object(pk)
        except Exception:
            return Response({'message': 'User does not exists '})
        try:
            connection = UserFollowing.objects.filter(user_id=user, following_user_id=follow).first()
            connection.delete()
        except Exception:
            return Response({'message': f"You don't follow {follow}"})
        # serializer = UserSerializer(follow)
        return Response({'message': f'You unfollowed {follow}'})


'''
Token Authentication needed so we use custome auth_token instead of ObatainAuthToken
because it gives more flexibility.
'''


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        if User.objects.filter(username=request.data['username']).exists():
            serializer = self.serializer_class(data=request.data,
                                               context={'request': request})
            if serializer.is_valid():
                user = serializer.validated_data['user']
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key,
                    'first_name': user.first_name,
                    # 'user_id': user.pk,
                    # 'email': user.email
                })
            return Response({"error": "Please check your Username or Password", "msg": "1"},
                            status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"error": "User does not exixts", "msg": "2"}, status=status.HTTP_404_NOT_FOUND)
