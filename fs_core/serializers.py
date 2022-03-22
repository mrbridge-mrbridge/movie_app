from rest_framework import serializers
from .models import *

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Movie
        fields = (
            'uuid',
            'title',
            'description',
            'date_added',
            'movie_type',
            'genre',
            'age_restriction',
            'get_absolute_url',
            'get_image',
            'get_thumbnail',
            'get_video',
            'videos',
        )

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
        
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = (
            'title',
            'get_video',
        )