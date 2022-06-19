from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

from .serializers import RegisterSerializer, MyTokenObtainPairSerializer
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer