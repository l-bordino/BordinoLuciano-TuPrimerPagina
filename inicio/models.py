from django.db import models


class Movie(models.Model):
    
    RATING_CHOICES = [(i, str(i)) for i in range(1, 11)]
    
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=50)
    length = models.IntegerField(default='en minutos')  # Length in minutes
    rating = models.IntegerField(choices=RATING_CHOICES, blank=True, null=True)
    
    def __str__(self):
        return f'{self.title} ({self.release_year}) - {self.director}'