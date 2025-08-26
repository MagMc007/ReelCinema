from rest_framework import serializers
from .models import Movie
from django.db.models import Avg, Count
from review.serializers import ReviewSerializer


class MovieSerializer(serializers.ModelSerializer):
    """ serializers movie data"""
    average_rating = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()
    recent_reviews = serializers.SerializerMethodField()

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
            "recent_reviews"
        ]
    
    def get_average_rating(self, obj):
        avg = obj.reviews.aggregate(avg=Avg("rating"))["avg"]
        if avg:
            return round(avg, 2)
        return None

    def get_reviews_count(self, obj):
        cnt = obj.reviews.aggregate(cnt=Count("id"))["cnt"]
        if cnt:
            return cnt
        return 0
    
    def get_recent_reviews(self, obj):
        reviews = obj.reviews.all().order_by("-created_at")[:5]
        return ReviewSerializer(reviews, many=True).data

