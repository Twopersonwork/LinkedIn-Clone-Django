from rest_framework import routers
from django.conf.urls import include
from django.urls import path
from .views import PostViewSet, create_post, LikeViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('likes', LikeViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create_post/', create_post),
]
# for setting the path for folder that will
# hold the uploaded images in Post model.
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                               document_root=settings.MEDIA_ROOT)
#     print(static(settings.MEDIA_URL,
#                               document_root=settings.MEDIA_ROOT))
