from django.urls import path, include
from inicio.views import create_movie, inicio, movie_list, movie_details, delete_movie, edit_movie

urlpatterns = [
    path('', inicio, name='inicio'),
    path('create-movie/', create_movie, name='create_movie'),
    path('movie-list/', movie_list, name='movie_list'),
    path('edit-movie/<int:movie_id>/', edit_movie, name='edit_movie'),
    path('delete-movie/<int:movie_id>/', delete_movie, name='delete_movie'),
    path('movie-details/<int:movie_id>/', movie_details, name='movie_details'),
]
