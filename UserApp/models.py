from django.db import models
from django.contrib.auth.models import User
from PostApp.models import Post

"""
Here, there are two main fiels.
user_id indicate user following and following_user_id indicate user followers.
"""


class UserFollowing(models.Model):
    user_id = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    following_user_id = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ["-created"]
