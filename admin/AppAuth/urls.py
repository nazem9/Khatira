from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


urlpatterns = [
    path('register',view=views.UserRegistration.as_view(),name = 'register'),
    path('login',view= views.UserLogin.as_view(),name='login'),
    path('logout',view=views.UserLogout.as_view(),name='logout'),
    path('user',view=views.UserView.as_view(),name = 'user')
]