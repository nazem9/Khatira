from django.contrib.auth import get_user_model,login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserLoginSerializer,UserRegistrationSerializer,UserSerializer,UserProfileSerializer
from rest_framework import permissions, status
from .validations import custom_validation,validate_username,validate_password
from .models import UserProfile,Language,Dialect

class UserRegistration(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self,request):
        clean_data = custom_validation(request.data)
        serializer = UserRegistrationSerializer(data = clean_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(clean_data)
            if user:
                return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self,request):
        data = request.data
        assert validate_username(data)
        assert validate_password(data)
        serializer = UserLoginSerializer(data = data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            login(request, user)
            return Response({},status=status.HTTP_200_OK)


class UserLogout(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)

class UserView(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)
	##
	def get(self, request):
		serializer = UserSerializer(request.user)
		return Response({'user': serializer.data}, status=status.HTTP_200_OK)
     
class UesrProfileView(APIView):
    def get(self,request):
        if request.user.is_authenticated:
            profile = UserProfile.objects.get(user = request.user.id)
            serializer = UserProfileSerializer(profile)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({"message":"you're not logged in!"},status=status.HTTP_403_FORBIDDEN)
        
    def post(self,request):
        if request.user.is_authenticated:
            profile = UserProfile.objects.get(user = request.user.id)
            serializer = UserProfileSerializer(profile)
            serializer.update(profile,validated_data=request.data)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({"message":"you're not logged in!"},status=status.HTTP_403_FORBIDDEN)

    def put(self,request):
        if request.user.is_authenticated:
            profile = UserProfile.objects.get(user = request.user.id)
            serializer = UserProfileSerializer(profile)
            serializer.update(profile,validated_data=request.data)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({"message":"you're not logged in!"},status=status.HTTP_403_FORBIDDEN)   