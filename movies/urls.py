from django.urls import path
from . import views


urlpatterns = [
    path("search/", views.MovieView.as_view(), name="movie-view"),
]