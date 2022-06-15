from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from . import serializers
from blog import models


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.filter(status='Published').order_by('-published_date')
    serializer_class = serializers.PostFetchSerializer
    #permission_classes = [permissions.IsAuthenticated]

