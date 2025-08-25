from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """ serializes the movie and review data """

    class Meta:
        model = Review
        fields = [
            "id",
            "user",
            "movie",
            "review_text",
            "rating",
            "created_at",
            "updated_at",
        ]

        read_only_fields = ["id", "user", "created_at", "updated_at"]
    
    def validate(self, data):
        """ ensure entered data for rating is in [1,5]"""
        if 1 > data["rating"] or data["rating"] > 5:
            raise serializers.ValidationError("Rating must be in the range [1, 5]")
        return data
