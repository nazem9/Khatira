from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField

class Language(models.Model):
    language = models.CharField(max_length=50,null=True)

class Dialect(models.Model):
    dialect = models.CharField( max_length=50,null=True)
    language =  models.ManyToManyField(Language,related_name='dialect_language',blank=True)



class UserProfile(models.Model):
    folowers = models.ManyToManyField(User,related_name='followed_by',symmetrical=False,blank=True)
    user = models.OneToOneField(User,related_name ='profile', on_delete=models.CASCADE)
    birth_date = models.DateField( auto_now=False, auto_now_add=False,null=True)
    phone_number = models.CharField( max_length=10, null = True)
    nationality = models.CharField( max_length=50,null=True)
    city = models.CharField( max_length=50,null=True)
    gender = models.BooleanField(null=True)
    accessibilty = models.BooleanField(null=True)
    languages = models.OneToOneField( Language ,on_delete=models.CASCADE,blank=True)
    dialect = models.ManyToManyField(Dialect,symmetrical=True,blank=True)

