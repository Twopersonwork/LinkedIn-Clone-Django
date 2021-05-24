from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import UserSerializer, UserFollowingSerializer, RegistrationSerializer,UserDetailSerializer
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import UserFollowing, User,WaitingList
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from django.db.models.signals import pre_save
from django.dispatch import receiver
import os

@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        data = {}

        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered new user.'
            # data['email'] = account.email
            # data['username'] = account.username
            # token = Token.objects.get(user=account).key
            # data['token'] = token
        else:
            data = serializer.errors
        return Response(data)


# First get the all the users and then display in a way mentioned in UserSerializers.
class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get','put','delete']

    # @receiver(pre_save, sender=User)
    # def delete_old_file(self,sender,attr,**kwargs):
    #     # on creation, signal callback won't be triggered
    #     if self._state.adding and not self.pk:
    #         return False
    #
    #     try:
    #         if attr=='profile_pic':
    #             old_file = sender.objects.get(pk=self.pk).profile_pic.file
    #         else:
    #             old_file = sender.objects.get(pk=self.pk).cover_pic.file
    #
    #     except sender.DoesNotExist:
    #         return False
    #     # comparing the new file with the old one
    #     if attr == 'profile_pic':
    #         file = self.profile_pic.file
    #     else:
    #         file = self.cover_pic.file
    #     print(type(old_file),old_file.name)
    #     if not old_file == file:
    #         if os.path.isfile(old_file.name):
    #             os.remove(old_file.name)

    @action(detail=True, methods=['PUT'])
    # this method is for update
    def update_user(self, request,pk=None):
        user = User.objects.get(id=pk)

        if 'profile_pic' in request.data:
            # old_file = User.objects.get(pk=user.pk).profile_pic.file
            # # comparing the new file with the old one
            # file = user.profile_pic.file
            # print(type(old_file), old_file.name)
            # if 'defaults'!=str(file).split("/")[-2]:
            #     if not old_file == file:
            #         if os.path.isfile(old_file.name):
            #             os.remove(old_file.name)
            print(request.data['profile_pic'])
            setattr(user, "profile_pic", request.data['profile_pic'])
            user.save()

        if 'cover_pic' in request.data:
            # old_file = User.objects.get(pk=user.pk).cover_pic.file
            # # comparing the new file with the old one
            # file = user.cover_pic.file
            # print(type(old_file), old_file.name)
            # if 'defaults'!=str(file).split("/")[-2]:
            #     if not old_file == file:
            #         if os.path.isfile(old_file.name):
            #             os.remove(old_file.name)
            # print(request.data['cover_pic'])
            setattr(user, "cover_pic", request.data['cover_pic'])
            user.save()


        if 'username' in request.data:
            setattr(user, "username", request.data['username'])
            user.save()
        serializer = UserSerializer(user,many=False)
        return Response(serializer.data)



    @action(detail=True, methods=['DELETE'])
    # this method is for update
    def delete_profile_pic(self, request, pk=None):
        user = User.objects.get(id=pk)
        user.profile_pic.delete(save=False)
        user.profile_pic = 'defaults/profile.svg'
        user.save()

        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    @action(detail=True, methods=['DELETE'])
    # this method is for update
    def delete_cover_pic(self, request, pk=None):
        user = User.objects.get(id=pk)
        user.cover_pic.delete(save=False)
        user.cover_pic = 'defaults/cover.jpg'
        user.save()

        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    # this method is for update
    def no_of_follow(self, request,pk=None,format=None):
        user = User.objects.get(id=pk)
        return Response({"no_followers":len(UserSerializer(user).data['followers']),"no_following": len(UserSerializer(user).data['following'])})

class UserDetailViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    http_method_names = ['get']

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
        # user = User.objects.get(pk=request.data['user'])
        user = request.user
        try:
            follow = self.get_object(pk)
        except Exception:
            return Response({'message': 'User does not exists '})
        try:
            if user != follow:
                UserFollowing.objects.create(user_id=user, following_user_id=follow)
            else:
                return Response({"message": "You can't follow yourself"})
        except Exception as e:
            return Response({"message": f"You already follow {follow}"})

        # serializer = UserSerializer(follow)
        return Response({'message': f'You follow {follow}'})

    # unfollow users.
    def delete(self, request, pk, format=None):
        # user = User.objects.get(pk=request.data['user'])
        user = request.user
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

class WaitFollow(APIView):
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
        # user = User.objects.get(pk=request.data['user'])
        user = request.user
        try:
            follow = self.get_object(pk)
        except Exception:
            return Response({'message': 'User does not exists '})
        try:
            if user != follow:
                WaitingList.objects.create(user_id=user, following_user_id=follow)
            else:
                return Response({"message": "You can't follow yourself"})
        except Exception as e:
            return Response({"message": f"You already follow {follow}"})

        # serializer = UserSerializer(follow)
        return Response({'message': f'You follow {follow}'})

    # unfollow users.
    def delete(self, request, pk, format=None):
        # user = User.objects.get(pk=request.data['user'])
        follow = request.user
        try:
            user = self.get_object(pk)
        except Exception:
            return Response({'message': 'User does not exists '})
        try:
            connection = WaitingList.objects.filter(user_id=user, following_user_id=follow).first()
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
        # in cutome User model email is essential for login but internally User takes
        # username attribute in django.
        if User.objects.filter(email=request.data['username']).exists():
            serializer = self.serializer_class(data=request.data,
                                               context={'request': request})
            print(request.data)
            if serializer.is_valid():
                print(request.data)
                user = serializer.validated_data['user']
                token, created = Token.objects.get_or_create(user=user)
                user_data = UserSerializer(user).data
                return Response({
                    'token': token.key,

                    'user': user_data,
                })

            return Response({"chk_uname_or_pwd": "Please check your Password"},
                            status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"user_not_found": "User does not exixts with this email address"},
                            status=status.HTTP_404_NOT_FOUND)
