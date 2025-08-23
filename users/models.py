from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ custom user model with additional fields """
    location = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username
