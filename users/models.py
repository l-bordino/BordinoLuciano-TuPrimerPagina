from django.db import models
from django.contrib.auth.models import User

from inicio.models import Movie


class AdditionalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    favorite_genre = models.CharField(max_length=20, 
                                      choices=Movie.GENRE_CHOICES, 
                                      null=True, 
                                      blank=True
                                      )