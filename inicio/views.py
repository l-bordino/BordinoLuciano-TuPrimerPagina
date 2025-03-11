from django.shortcuts import redirect, render
from inicio.forms import CreateMovie, FindMovie, EditMovie
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
            
            
            return redirect('movie_list')
    
    return render(request, 'inicio/create_movie.html', {'formulario': formulario})
    
def movie_list(request):
    movies = Movie.objects.all()
    formulario = FindMovie(request.GET)
    if formulario.is_valid():
        movie_by_title = formulario.cleaned_data.get('title')
        movie_by_director = formulario.cleaned_data.get('director')
        movie_by_release_year = formulario.cleaned_data.get('release_year')
        movie_by_length = formulario.cleaned_data.get('length')
        movie_by_genre = formulario.cleaned_data.get('genre')
        movie_by_rating = formulario.cleaned_data.get('rating')
        
        filtro = {}
        if movie_by_title:
            filtro["title__icontains"] = movie_by_title
        if movie_by_director:
            filtro["director__icontains"] = movie_by_director
        if movie_by_release_year:
            filtro["release_year__exact"] = movie_by_release_year
        if movie_by_length:
            filtro["length__lte"] = movie_by_length
        if movie_by_rating:
            filtro["rating__gt"] = movie_by_rating
        if movie_by_genre:
            filtro["genre__exact"] = movie_by_genre
        
        if filtro:    
            movies = Movie.objects.filter(**filtro)
        
    return render(request, 'inicio/movie_list.html', {'movies': movies, 'formulario': formulario})

def delete_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie.delete()
    return redirect('movie_list')
    
def movie_details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'inicio/movie_details.html', {'movie': movie} )

def edit_movie(request, movie_id):
    
    movie = Movie.objects.get(id=movie_id)
    
    if request.method == "POST":
        formulario = EditMovie(request.POST, instance=movie)
        if formulario.is_valid():
            formulario.save()
        return redirect('movie_list')
    else:
        formulario = EditMovie(instance=movie)
    return render(request, 'inicio/edit_movie.html', {'formulario': formulario})
            