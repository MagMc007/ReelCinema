from .views import SignUpView
from django.urls import path

app_name = "users"

urlpatterns = [
    path("register/", SignUpView.as_view(), name="register-view"),
]