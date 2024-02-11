from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField

class Language(models.Model):
    language = models.CharField(max_length=50, null=True)

    def __str__(self) -> str:
        return self.language.__str__()

class Dialect(models.Model):
    dialect = models.CharField(max_length=50, null=True)
    language = models.ManyToManyField(Language, related_name='dialect_languages', blank=True)
    def __str__(self) -> str:
        return self.dialect.__str__()

class UserProfile(models.Model):
    followers = models.ManyToManyField(User, related_name='followed_by', symmetrical=False, blank=True)
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    birth_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    phone_number = models.CharField(max_length=10, null=True)
    nationality = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    gender = models.BooleanField(null=True)
    accessibility = models.BooleanField(null=True)
    languages = models.ManyToManyField(Language, related_name='user_profiles', blank=True)
    dialects = models.ManyToManyField(Dialect, related_name='user_profiles', blank=True)
