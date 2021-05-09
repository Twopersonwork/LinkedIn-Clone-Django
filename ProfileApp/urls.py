from rest_framework import routers
from django.conf.urls import include
from django.urls import path
from .views import ProfileViewSet, EducationViewSet, LicenseViewSet,SkillViewSet,AboutViewSet

router = routers.DefaultRouter()
router.register('user_profile', ProfileViewSet)
router.register('education', EducationViewSet)
router.register('license', LicenseViewSet)
router.register('skills',SkillViewSet)
router.register('about',AboutViewSet)

urlpatterns = [
    path('', include(router.urls))]
