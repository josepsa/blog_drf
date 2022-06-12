from rest_framework import serializers
from blog import models

class PostFetchSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=models.Post