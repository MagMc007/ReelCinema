from rest_framework import generics, status
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    """ provides view for registering """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    authentication_classes = []  

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        username = response.data["username"]
        user = User.objects.get(username=username)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "TOKEN": token.key,
            "username": user.username,
            "email": user.email,
            "location": user.location,
            "date_of_birth": user.date_of_birth,
        }, status=status.HTTP_201_CREATED)
    

class LoginView(APIView):
    """ logs in a user with credentials  """
    permission_classes = [AllowAny]
    authentication_classes = []  

    # implements post and use serializer for authentication checking
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "TOKEN": token.key,
            "user_id": user.id,
            "username": user.username
            },
            status=status.HTTP_200_OK
        )