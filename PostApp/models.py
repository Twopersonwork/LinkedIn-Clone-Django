import datetime
from django.db import models
from django.conf import settings


# Cascasde : if any user will be deleted the post
# corresponding to that will also be deleted.



class Post(models.Model):
    body = models.TextField(max_length=500)
    image = models.ImageField(null=True,blank=True,upload_to='post_images/',default=None)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='posts',on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.datetime.today)

    class Meta:
        ordering = ["-date"]

    def no_of_like(self):
        likes = Like.objects.filter(post=self)
        return len(likes)

    def no_of_comment(self):
        comments = Comment.objects.filter(post=self)
        return len(comments)

    # def has_liked_post(self):
    #     if Like.objects.filter(user=self.user,post=self).count() > 0:
    #         return True
    #     else:
    #         return False





# if any post or user will be deleted, the 'like' row
# corresponding to that will also be deleted.
class Like(models.Model):
    post = models.ForeignKey(Post,related_name='likes',on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    class Meta:
        # unique_together means same user can not like the same post more than once.
        unique_together = (('user', 'post'),)
        index_together = (('user', 'post'),)


# Comment table which is store the information about User and Post.
class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)