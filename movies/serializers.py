from rest_framework import serializers
from .models import Movie
from django.db.models import Avg, Count


class MovieSerializer(serializers.ModelSerializer):
    """ serializers movie data"""
    average_rating = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = [
            "id", 
            "title",
            "year",
            "imdb_id",
            "type",
            "poster",
            "average_rating",
            "reviews_count",
        ]
    
    def get_average_rating(self, obj):
        avg = obj.reviews.aggregate(avg=Avg("rating"))["avg"]
        return round(avg, 2) or None

    def get_reviews_count(self, obj):  # match field name
        cnt = obj.reviews.aggregate(cnt=Count("id"))["cnt"]
        return cnt or 0
    

