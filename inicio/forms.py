from django import forms
from inicio.models import Movie

class CreateMovie(forms.Form):
    title = forms.CharField(max_length=100)
    director = forms.CharField(max_length=100)
    release_year = forms.IntegerField()
    genre = forms.ChoiceField(choices=[("", "---")] + Movie.GENRE_CHOICES)
    length = forms.IntegerField() 
    rating = forms.ChoiceField(choices=[("", "---")] + Movie.RATING_CHOICES, required=False)
    
class FindMovie(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    director = forms.CharField(max_length=100, required=False)
    release_year = forms.IntegerField(required=False)
    length = forms.IntegerField(required=False) 
    genre = forms.ChoiceField(choices=[("", "Seleccione un género")] + Movie.GENRE_CHOICES, required=False)
    rating = forms.ChoiceField(choices=[("", "Seleccione un rating")] + Movie.RATING_CHOICES, required=False)