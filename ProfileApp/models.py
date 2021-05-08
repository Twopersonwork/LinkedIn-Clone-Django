from django.db import models
from UserApp.models import User


# All user profile details..
class Profile(models.Model):
    user = models.OneToOneField(User, related_name="user_profile", on_delete=models.CASCADE)
    firstName = models.CharField(max_length=25, blank=True, null=True)
    lastName = models.CharField(max_length=25, blank=True, null=True)
    headLine = models.CharField(max_length=100, blank=True, null=True)
    education = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=40, blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)


# User about
class About(models.Model):
    user = models.OneToOneField(User, related_name="user_about", on_delete=models.CASCADE)
    about = models.TextField(max_length=2000, blank=True, null=True)


# User education
class Education(models.Model):
    user = models.ForeignKey(User, related_name="user_education", on_delete=models.CASCADE)
    school = models.CharField(max_length=100, blank=True, null=True)
    degree = models.CharField(max_length=100, blank=True, null=True)
    field_of_study = models.CharField(max_length=100, blank=True, null=True)
    start_year = models.CharField(max_length=4, blank=True, null=True)
    end_year = models.CharField(max_length=4, blank=True, null=True)


# For user license and certifications
class License(models.Model):
    user = models.ForeignKey(User, related_name="user_license", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    issuing_org = models.CharField(max_length=200, blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    expiration_date = models.DateField(blank=True,null=True)
    credential_id = models.CharField(max_length=100, blank=True, null=True)


# For user skills and endorsements
class Skill(models.Model):
    user = models.ForeignKey(User, related_name="user_skills", on_delete=models.CASCADE)
    skill = models.CharField(max_length=100,blank=True,null=True)

    class Meta:
        unique_together = ['user', 'skill']