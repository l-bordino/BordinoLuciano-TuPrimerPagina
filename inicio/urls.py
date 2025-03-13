from django.urls import path, include
from inicio.views import MovieUpdateView, MovieDeleteView, create_movie, inicio, movie_list, movie_details

urlpatterns = [
    #region urls normales
    path('', inicio, name='inicio'),
    path('create-movie/', create_movie, name='create_movie'),
    path('movie-list/', movie_list, name='movie_list'),
    path('movie-details/<int:movie_id>/', movie_details, name='movie_details'),
    # path('edit-movie/<int:movie_id>/', edit_movie, name='edit_movie'),
    # path('delete-movie/<int:movie_id>/', delete_movie, name='delete_movie'),
    #endregion
    #region urls CBV
    path('edit-movie/<int:pk>/', MovieUpdateView.as_view(), name='edit_movie'),
    path('delete-movie/<int:pk>/', MovieDeleteView.as_view(), name='delete_movie'),
    #endregion
]
