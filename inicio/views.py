from django.shortcuts import redirect, render
from inicio.forms import CreateMovie, FEditMovie, FindMovie
from inicio.models import Movie
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Case, When, Value, IntegerField

# region vistas comunes

def inicio(request):
    has_movies = False
    if request.user.is_authenticated:
        # Filtra las películas por el usuario actual
        has_movies = Movie.objects.filter(user=request.user).exists()
    
    return render(request, 'inicio/inicio.html', {'has_movies': has_movies})

@login_required 
def create_movie(request):
    formulario = CreateMovie()
    
    if request.method == 'POST':
        formulario = CreateMovie(request.POST, request.FILES)
        if formulario.is_valid():
            title = formulario.cleaned_data.get('title')
            director = formulario.cleaned_data.get('director')
            release_year = formulario.cleaned_data.get('release_year')
            genre = formulario.cleaned_data.get('genre')
            length = formulario.cleaned_data.get('length')
            rating = formulario.cleaned_data.get('rating')
            poster = formulario.cleaned_data.get('poster')
            
            if rating == '':
                rating = None
            
            movie = Movie(title=title, director=director, release_year=release_year, genre=genre, length=length, rating=rating, poster=poster, user = request.user)
            movie.save()
            
            
            return redirect('movie_list')
    
    return render(request, 'inicio/create_movie.html', {'formulario': formulario})
   

@login_required 
def movie_list(request):
    movies = Movie.objects.filter(user=request.user)
    formulario = FindMovie(request.GET)

    favorite_genre = None
    if request.user.is_authenticated and hasattr(request.user, 'additionalinfo'):
        favorite_genre = request.user.additionalinfo.favorite_genre

    # Filtrado según los criterios del formulario
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

    # Priorizar películas del género favorito
    if favorite_genre:
        movies = movies.annotate(
            is_favorite=Case(
                When(genre=favorite_genre, then=Value(1)),
                default=Value(0),
                output_field=IntegerField()
            )
        ).order_by('-is_favorite', 'title')  # Primero favoritas, luego por título

    return render(request, 'inicio/movie_list.html', {'movies': movies, 'formulario': formulario})

@login_required   
def movie_details(request, movie_id):
    movie = Movie.objects.filter(id=movie_id, user=request.user).first()
    if not movie:
        return redirect('movie_list')  # Redirige si no encuentra la película o no pertenece al usuario
    
    return render(request, 'inicio/movie_details.html', {'movie': movie})

def about_me(request):
    return render(request, 'inicio/about_me.html')
# endregion

# region CBV

class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = Movie
    template_name = 'inicio/CBV/edit_movie.html'
    form_class = FEditMovie
    success_url = reverse_lazy('movie_list')

    
class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie
    template_name = 'inicio/CBV/delete_movie.html'
    success_url = reverse_lazy('movie_list')
    

# endregion