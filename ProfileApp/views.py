from rest_framework import viewsets
from .models import Profile, Education, License, Skill, About
from .serializers import ProfileSerializers, EducationSerializers, LicenseSerializer, SkillSerializer, AboutSerializers
from rest_framework.permissions import IsAuthenticated


# post,get,put all the operation done here for profile
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers
    permission_classes = [IsAuthenticated]

    # this method is for update
    def put(self, request, pk, *args, **kwargs):
        return self.update(request, pk, *args, **kwargs)


# post,get,put all the operation done here for about
class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializers
    permission_classes = [IsAuthenticated]

    def put(self, request, pk, *args, **kwargs):
        return self.update(request, pk, *args, **kwargs)


# post,get,put all the operation done here for education
class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializers
    permission_classes = [IsAuthenticated]

    # this method is for update
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


# post,get,put all the operatiob done here for license and certificate
class LicenseViewSet(viewsets.ModelViewSet):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer
    permission_classes = [IsAuthenticated]

    # this method is for update
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


# post,get,put all operation done here for skills and endorsement
class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

    # this method is for update
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
