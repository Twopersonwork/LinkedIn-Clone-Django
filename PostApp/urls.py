from rest_framework import routers
from django.conf.urls import include
from django.urls import path
from .views import PostViewset,create_post,LikeViewset
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('posts',PostViewset)
router.register('likes',LikeViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('create_post/',create_post)
]
# for setting the path for folder that will
# hold the uploaded images in Post model.
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

