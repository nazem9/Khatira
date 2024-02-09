from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from .models import UserProfile,Language,Dialect
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
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class DialectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dialect
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    languages = LanguageSerializer(many=True)  # Treat languages as a nested serializer
    dialects = DialectSerializer(many=True)

    class Meta:
        model = UserProfile
        fields = '__all__'

    def create(self, validated_data):
        languages_data = validated_data.pop('languages')
        dialects_data = validated_data.pop('dialects')

        user_profile = UserProfile.objects.create(**validated_data)

        languages_instances = [Language.objects.create(**lang_data) for lang_data in languages_data]
        dialects_instances = [Dialect.objects.create(**dialect_data) for dialect_data in dialects_data]

        user_profile.languages.set(languages_instances)
        user_profile.dialects.set(dialects_instances)

        return user_profile

    def update(self, instance, validated_data):
        languages_data = validated_data.pop('languages', None)
        dialects_data = validated_data.pop('dialects', None)

        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.nationality = validated_data.get('nationality', instance.nationality)
        instance.city = validated_data.get('city', instance.city)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.accessibility = validated_data.get('accessibility', instance.accessibility)

        if languages_data:
            languages_instances = [Language.objects.create(**lang_data) for lang_data in languages_data]
            instance.languages.set(languages_instances)

        if dialects_data:
            dialects_instances = [Dialect.objects.create(**dialect_data) for dialect_data in dialects_data]
            instance.dialects.set(dialects_instances)

        instance.save()
        return instance