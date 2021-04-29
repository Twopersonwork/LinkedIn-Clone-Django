from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


'''
Validation of email . Using user model you can get the user
and create the user.
'''

class UserSerializer(serializers.ModelSerializer):
    # for validate user email
    def validate_email(self,value):
        lower_email = value.lower()
        if User.objects.filter(email=lower_email).exists():
            raise serializers.ValidationError("Email already exists")
        return lower_email

    class Meta:
        model = User
        fields = ['id', 'first_name','username','last_name','email', 'password','date_joined']
        # extra_kwargs for validation on some fields.
        extra_kwargs = {'password': {'write_only': True, 'required': True},
                        'first_name':{'required':True},'last_name':{'required':True},
                        'email':{'required':True}
                        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)  # create user
        Token.objects.create(user=user)                     # create token for particular user
        return user