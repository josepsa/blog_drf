from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

from .serializers import RegisterSerializer
from rest_framework import generics


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer