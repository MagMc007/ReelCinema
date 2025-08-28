from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.views import APIView
import requests
from rest_framework.permissions import AllowAny

OMDB_KEY = "58c421c3"


class MovieView(APIView):
    """ provides view for movies by title"""
    permission_classes = [AllowAny]
    authentication_classes = []  

    def get(self, request):
        # get the title
        title = request.query_params.get("title")
        if not title:
            return Response(
                {"Error": "Enter movie title"}, status=400
            )
        # fetch the first movie from database using title

        movie = Movie.objects.filter(title__iexact=title).first()
        if movie:
            # serialize the movie data

            serializer = MovieSerializer(movie)
            return Response(
                serializer.data
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
            movie, created = Movie.objects.get_or_create(
                imdb_id = search_value["imdbID"],
                defaults = {
                    "title": search_value["Title"],
                    "year": search_value["Year"],
                    "type": search_value["Type"],
                    "poster": search_value["Poster"]
                    }
            )
            serialized_movie = MovieSerializer(movie)
            return Response(
                serialized_movie.data
            )

        return Response({"error": "Movie not found"}, status=404)




