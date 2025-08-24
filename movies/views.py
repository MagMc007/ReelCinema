from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.views import APIView
import requests

OMDB_KEY = "58c421c3"


class MovieView(APIView):
    """ provides view for movies by title"""
    def get(self, request, title):
        # fetch movie from database using title

        movie = Movie.objects.filter(title=title)
        if movie:
            # serialize the movie data

            movie = MovieSerializer(movie)
            return Response(
                movie.data
            )
        
        # if not in db fetch from OMDB
        url = f"http://www.omdbapi.com/?apikey=[{OMDB_KEY}]&s={title}"
        r = requests.get(url)
        data = r.json()

        # check the OMDB response
        if data.Response:
            # create the movie in db first
            Movie.objects.create(
                "title": data["Title"],
                "year": data["Year"],
                "imdb_id": data["imdbID"],
                "type": data["Type"],
                "poster": data["Poster"]
            )
            return Response(
                MovieSerializer(data)
            )

        return Response({"error": "Movie not found"}, status=404)




