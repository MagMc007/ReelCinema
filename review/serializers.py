from rest_framework import serializers
from .models import Review
from users.serializers import UserSerializer
from movies.models import Movie


class ReviewSerializer(serializers.ModelSerializer):
    """ serializes the movie and review data """
    user = UserSerializer(read_only=True)
    movie_id = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all(), write_only=True, source='movie'
    )

    class Meta:
        model = Review
        fields = [
            "id",
            "user",
            "movie_id",
            "review_text",
            "rating",
            "created_at",
            "updated_at",
        ]

        read_only_fields = ["id", "user", "created_at", "updated_at"]
    
    def validate(self, data):
        """ ensure entered data for rating is in [1,5]"""
        if 1 > data["rating"] or data["rating"] > 5:
            raise serializers.ValidationError("Rating must be in the range [1,5]")
        return data 
