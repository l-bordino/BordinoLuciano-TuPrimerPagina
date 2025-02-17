from django.urls import path, include
from inicio.views import create_movie, inicio, movie_list 

urlpatterns = [
    path('', inicio, name='inicio'),
    path('create-movie/', create_movie, name='create_movie'),
    path('movie-list/', movie_list, name='movie_list'),
]
