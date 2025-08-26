from rest_framework import serializers
from .models import Review
from users.serializers import UserSerializer
from movies.models import Movie
from django.contrib.auth import get_user_model

User = get_user_model()


class ReviewerUserSerializer(serializers.ModelSerializer):
    """ provides serialized user data to be included in the review"""
    class Meta:
        model = User
        fields = ["username", "email"]


class ReviewSerializer(serializers.ModelSerializer):
    """ serializes the movie and review data """
    user = ReviewerUserSerializer(read_only=True)
    movie_id = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all(), write_only=True, source='movie'
    )
    title = serializers.CharField(source="movie.title", read_only=True) 

    class Meta:
        model = Review
        fields = [
            "id",
            "user",
            "movie_id",
            "title",
            "review_text",
            "rating",
            "created_at",
            "updated_at",
        ]

        read_only_fields = ["id", "user", "created_at", "updated_at", "title"]
    
    def validate(self, data):
        """ ensure entered data for rating is in [1,5] """

        if 1 > data["rating"] or data["rating"] > 5:
            raise serializers.ValidationError("Rating must be in the range [1,5]")
        return data 
    
    def update(self, instance, validated_data):
        """ allows editing review_text and rating """
        instance.review_text = validated_data.get("review_text", instance.review_text)
        instance.rating = validated_data.get("rating", instance.rating)
        instance.save()
        return instance

    


