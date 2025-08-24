from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    """ serializers movie data"""
    class Meta:
        model = Movie
        fields = "__all__"