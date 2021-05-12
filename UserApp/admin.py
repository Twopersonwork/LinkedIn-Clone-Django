from django.contrib import admin
from .models import UserFollowing,User,WaitingList
# from django.contrib.auth.admin import UserAdmin


admin.site.register(User)
# Register your models here.

admin.site.register(UserFollowing)
admin.site.register(WaitingList)


