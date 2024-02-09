from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    def create(self,clean_data):
        user_obj = User.objects.create_user(username=clean_data['username'],
                                 email=clean_data['email'],
                                 password=clean_data['password'])
        user_obj.save()
        return user_obj
    
class UserLoginSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField()
    password = serializers.CharField()
    username = serializers.CharField()
    class Meta:
        model = User
        fields = ['password', 'username']

    def check_user(self,clean_data):
        user = authenticate(username = clean_data['username'],password = clean_data['password'])
        if not user:
            raise ValidationError("User not found")
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','username')