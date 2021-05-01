from rest_framework import routers
from django.conf.urls import include
from django.urls import path
from .views import UserViewset, UserFollowingViewSet, UserFollow

router = routers.DefaultRouter()

# Here, creating routes for different viewsets.
router.register('users', UserViewset)
router.register('userfollowings', UserFollowingViewSet,
                basename='userfollowing')  # to see all the details of followe and following.

urlpatterns = [
    path('', include(router.urls)),
    path('follow/<int:pk>/', UserFollow.as_view(), name='user-follow'),  # to Follow,Get the detail, Unfollow
]
