from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import User
from .models import UserFollowing
from PostApp.serializers import PostSerializer


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        account = User(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        account.set_password(password)
        account.save()
        return account
'''
Validation of email . Using user model you can get the user
and create the user.
'''

class UserSerializer(serializers.ModelSerializer):
    # Adding this field into User's fields.
    following = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()
    posts = PostSerializer(read_only=True,many=True)
    # for validate user email
    def validate_email(self, value):
        lower_email = value.lower()
        if User.objects.filter(email=lower_email).exists():
            raise serializers.ValidationError("Email already exists")
        return lower_email

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'date_joined', 'following',
                  'followers','posts','profile_pic']
        # extra_kwargs for validation on some fields.
        extra_kwargs = {'password': {'write_only': True, 'required': True},
                        'email': {'required': True}
                        }

    # using FollowingSerializer we can get all the details of following for particular user.
    def get_following(self, obj):
        return FollowingSerializer(obj.following.all(), many=True).data

    # using FollowersSerializer we can get all the details of followers for particular user.

    def get_followers(self, obj):
        return FollowersSerializer(obj.followers.all(), many=True).data

    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)  # create user
    #     Token.objects.create(user=user)  # create token for particular user
    #     return user


"""
You can see the follower and following using this serializer.
"""
class UserFollowingSerializer(serializers.ModelSerializer):
    following = serializers.ReadOnlyField(source='following_user_id.username')
    follower = serializers.ReadOnlyField(source='user_id.username')

    class Meta:
        model = UserFollowing
        fields = ['id', 'created', 'following', 'follower']


"""
FollowingSerializer for particular field for following.
"""
class FollowingSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='following_user_id.username')  # to get the username of following_user_id

    class Meta:
        model = UserFollowing
        fields = ['id', 'following_user_id', 'username', 'created']


"""
FollowerSerializer for particular field for follower.
"""

class FollowersSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user_id.username')  # to get the username of user_id

    class Meta:
        model = UserFollowing
        fields = ['id', 'user_id', 'username', 'created']


