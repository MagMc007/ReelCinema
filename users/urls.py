from .views import SignUpView, SingInView, dummy, LogoutView, userChangeView
from django.urls import path

app_name = "users"

urlpatterns = [
    path("register/", SignUpView.as_view(), name="register-view"),
    path("login/", SingInView.as_view(), name="login-view"),
    path("dummy/", dummy, name="dummy"),
    path("logout/", LogoutView.as_view(), name="logout-view"),
    path("change/", userChangeView, name="change-view"),
]