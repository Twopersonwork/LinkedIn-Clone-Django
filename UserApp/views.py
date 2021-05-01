from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status





# First get the all the users and then display in a way mentioned in UserSerializers.
class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer








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
                    'first_name':user.first_name,
                    # 'user_id': user.pk,
                    # 'email': user.email
                })
            return Response({"error": "Please check your Username or Password", "msg": "1"},
                            status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"error": "User does not exixts", "msg": "2"}, status=status.HTTP_404_NOT_FOUND)
