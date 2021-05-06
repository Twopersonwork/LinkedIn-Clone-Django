from django.contrib import admin
from .models import Profile, Education, License, Skill,About

# Register your models here.
admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(License)
admin.site.register(Skill)
admin.site.register(About)