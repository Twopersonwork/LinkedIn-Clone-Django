from rest_framework import routers
from django.conf.urls import include
from django.urls import path
from .views import UserViewset


router = routers.DefaultRouter()

# Here, creating routes for different viewsets.
router.register('users',UserViewset)

urlpatterns = [
    path('',include(router.urls)),
]
