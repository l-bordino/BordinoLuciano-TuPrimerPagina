from django import forms
from inicio.models import Movie

class CreateMovie(forms.Form):
    title = forms.CharField(max_length=100)
    director = forms.CharField(max_length=100)
    release_year = forms.IntegerField()
    genre = forms.CharField(max_length=50)
    length = forms.IntegerField() 
    rating = forms.ChoiceField(choices=Movie.RATING_CHOICES, widget=forms.Select(), required=False)
    
class FindMovie(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    director = forms.CharField(max_length=100, required=False)