from django.contrib import admin
from .models import Post,Like
# Register your models here.

# so we can see these at django Development Server.
admin.site.register(Post)
admin.site.register(Like)