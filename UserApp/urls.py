from rest_framework import routers
from django.conf.urls import include
from django.urls import path
from .views import UserViewset, UserFollowingViewSet, UserFollow, registration_view

router = routers.DefaultRouter()

# Here, creating routes for different viewsets.
router.register('users', UserViewset)
# to see all the details of follow and following.
router.register('userfollowings', UserFollowingViewSet, basename='userfollowing')

urlpatterns = [
    path('', include(router.urls)),
    # to Follow,Get the detail, Unfollow
    path('follow/<int:pk>/', UserFollow.as_view(), name='user-follow'),
    path('register/', registration_view),


]
