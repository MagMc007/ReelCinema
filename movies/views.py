from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.views import APIView
import requests

OMDB_KEY = "58c421c3"


class MovieView(APIView):
    """ provides view for movies by title"""
    def get(self, request, title):
        # fetch the first movie from database using title

        movie = Movie.objects.filter(title__iexact=title).first()
        if movie:
            # serialize the movie data

            movie = MovieSerializer(movie)
            return Response(
                movie.data
            )
        
        # if not in db fetch from OMDB
        url = f"http://www.omdbapi.com/?apikey={OMDB_KEY}&s={title}"
        r = requests.get(url)
        data = r.json()

        # check the OMDB response
        if data.get("Response") == "True":
            # separate movie from rest of json response
            search_value = data["Search"][0]

            # create the movie in db first
            movie = Movie.objects.create(
                title=search_value["Title"],
                year=search_value["Year"],
                imdb_id=search_value["imdbID"],
                type=search_value["Type"],
                poster=search_value["Poster"]
            )
            serialized_movie = MovieSerializer(movie)
            return Response(
                serialized_movie.data
            )

        return Response({"error": "Movie not found"}, status=404)




