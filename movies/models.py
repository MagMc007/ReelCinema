from django.db import models


class Movie(models.Model):
    """ represents movies fetched from OMDB"""
    title = models.CharField(max_length=250)
    year = models.CharField(max_length=50) # to handle series with year range
    imdb_id = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=50)
    poster = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} from {self.year}"