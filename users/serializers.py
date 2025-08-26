from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """serializers user data"""

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "location",
            "date_of_birth",
        ]


class RegisterSerializer(serializers.ModelSerializer):
    """serializers user registry data"""

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "location",
            "date_of_birth",
        ]

    # overide the user creation process 

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"],
            date_of_birth=validated_data["date_of_birth"],
            location=validated_data["location"],
        )

        # create the token for the user
        Token.objects.get_or_create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    """ serializes login data """

    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    # validate the inserted data
    def validate(self, data):
        user = authenticate(username=data["username"], password=data["password"])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credential")
