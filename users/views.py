from rest_framework import generics, status
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


class RegisterView(generics.CreateAPIView):
    """ provides view for registering """

    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        return serializer.save()
    

class LoginView(APIView):
    """ logs a user with credentials in """

    # implements post and use serializer for authentication checking
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "token": token.key,
            "user_id": user.id,
            "username": user.username
            },
            status=status.HTTP_200_OK
        )