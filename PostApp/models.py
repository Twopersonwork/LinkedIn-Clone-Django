from django.db import models
from django.contrib.auth.models import User


# Cascasde : if any user will be deleted the post
# corresponding to that will also be deleted.
class Post(models.Model):
    body = models.TextField(max_length=500)
    image = models.ImageField(null=True, blank=True, upload_to='post_images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def no_of_like(self):
        likes = Like.objects.filter(post=self)
        return len(likes)


# if any post or user will be deleted, the 'like' row
# corresponding to that will also be deleted.
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        # unique_together means same user can not like the same post more than once.
        unique_together = (('user', 'post'),)
        index_together = (('user', 'post'),)
