from django.shortcuts import render
from inicio.forms import CreateMovie, FindMovie
from inicio.models import Movie

def inicio(request):
    return render(request, 'inicio/inicio.html')

def create_movie(request):
    formulario = CreateMovie()
    
    if request.method == 'POST':
        formulario = CreateMovie(request.POST)
        if formulario.is_valid():
            title = formulario.cleaned_data.get('title')
            director = formulario.cleaned_data.get('director')
            release_year = formulario.cleaned_data.get('release_year')
            genre = formulario.cleaned_data.get('genre')
            length = formulario.cleaned_data.get('length')
            rating = formulario.cleaned_data.get('rating')
            
            if rating == '':
                rating = None
            
            movie = Movie(title=title, director=director, release_year=release_year, genre=genre, length=length, rating=rating)
            movie.save()
            
            
    
    return render(request, 'inicio/create_movie.html', {'formulario': formulario})
    
def movie_list(request):
    movies = Movie.objects.all()
    formulario = FindMovie(request.GET)
    if formulario.is_valid():
        movie_by_title = formulario.cleaned_data.get('title')
        movie_by_director = formulario.cleaned_data.get('director')
        movies = Movie.objects.filter(title__icontains=movie_by_title, director__icontains=movie_by_director)
    return render(request, 'inicio/movie_list.html', {'movies': movies, 'formulario': formulario})