from django.db import models


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
    
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    release_year = models.DateField()
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    length = models.IntegerField() 
    rating = models.IntegerField(choices=RATING_CHOICES, blank=True, null=True)
    
    def __str__(self):
        
        if self.rating:
            self.rating = '('+str(self.rating)+'*)'
        else:
            self.rating=''
            
        if self.release_year:
            self.release_year = self.release_year.year
            
        return f'"{self.title}" ({self.release_year}) - {self.director} [{self.length} m]. {self.rating}'