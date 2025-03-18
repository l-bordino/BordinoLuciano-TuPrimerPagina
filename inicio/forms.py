from django import forms
from inicio.models import Movie

class CreateMovie(forms.Form):
    title = forms.CharField(max_length=100)
    director = forms.CharField(max_length=100)
    release_year = forms.DateField(required=False, widget=forms.DateInput(attrs={'type':'date'}))
    genre = forms.ChoiceField(choices=[("", "----------")] + Movie.GENRE_CHOICES)
    length = forms.IntegerField() 
    rating = forms.ChoiceField(choices=[("", "---")] + Movie.RATING_CHOICES, required=False)
    poster = forms.ImageField(required=False)
    
class FindMovie(forms.Form):
    title = forms.CharField(max_length=100, required=False, label='Título')
    director = forms.CharField(max_length=100, required=False, label="Director/x/s")
    release_year = forms.DateField(required=False, widget=forms.DateInput(attrs={'type':'date'}), label="Fecha de estreno")
    length = forms.IntegerField(required=False, label='Duración (en minutos)') 
    genre = forms.ChoiceField(choices=[("", "----------")] + Movie.GENRE_CHOICES, required=False, label="Género")
    rating = forms.ChoiceField(choices=[("", "---")] + Movie.RATING_CHOICES, required=False,label='Puntaje')
    
class FEditMovie(forms.ModelForm):
    
    release_year = forms.DateField(required=False, widget=forms.DateInput(attrs={'type':'date'}))
    poster = forms.ImageField(required=False)

    class Meta:
        model = Movie
        fields = ['title', 'director', 'release_year', 'genre', 'length', 'rating', 'poster' ]