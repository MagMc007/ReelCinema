from django.db import models
from django.contrib.auth import get_user_model
from movies.models import Movie


User = get_user_model()


class Review(models.Model):
    """ handle reviews from user on movies """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    review_text = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # verify 1 review per user per movie
        # contain review b/n 1-5
        constraints = [
            models.CheckConstraint(check=models.Q(rating__gte=1, rating__lte=5), name="rating_range"),
            models.UniqueConstraint(fields=['user', 'movie'], name="movie_user_unique"),
        ]
    
    def __str__(self):
        return f"{self.user.username} -> {self.movie.title} :{self.rating}"

    

