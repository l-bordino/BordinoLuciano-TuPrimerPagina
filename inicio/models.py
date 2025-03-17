from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    
    RATING_CHOICES = [(i, str(i)) for i in range(1, 11)]
    GENRE_CHOICES = [
        ('accion', 'Acción'),
        ('drama', 'Drama'),
        ('terror', 'Terror'),
        ('comedia', 'Comedia'),
        ('belica', 'Bélica'),
        ('romantica', 'Romántica'),
        ('animacion', 'Animación'),
        ('aventura', 'Aventura'),
        ('fantasia', 'Fantasía'),
        ('misterio', 'Misterio'),
        ('musical', 'Musical'),
        ('thriller', 'Thriller'),
        ('ciencia_ficcion', 'Ciencia Ficción'),
        ('otro', 'Otro'), 
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movies')
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    release_year = models.DateField(blank=True, null=True)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    length = models.IntegerField() 
    rating = models.IntegerField(choices=RATING_CHOICES, blank=True, null=True)
    poster = models.ImageField(upload_to='posters', null=True, blank=True)
    
    def __str__(self):
            
        return f'" {self.title}" ({self.release_year.year or ''}) - {self.director} [{self.length} m]. {self.rating or ''}'