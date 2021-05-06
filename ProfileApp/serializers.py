from rest_framework import serializers
from .models import Profile, Education, License, Skill, About


# This serializer is for display all the details of profile of particular users
class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


# This serializer is for displau About information of the user.
class AboutSerializers(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"


# This serializer is for display all the details of education of particular users
class EducationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"


# This serializer is for display all the details of license and certification of the particular users
class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = "__all__"


# This serializer is for display all the details of skills and endorsement of particular users.
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
