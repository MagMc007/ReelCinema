from django.urls import path
from . import views


urlpatterns = [
    path("search/<str:title>", views.MovieView, name="movie-view"),
]