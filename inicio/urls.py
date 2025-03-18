from django.urls import path, include
from inicio.views import MovieDeleteView, MovieUpdateView, create_movie, inicio, movie_list, movie_details, about_me
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #region urls normales
    path('', inicio, name='inicio'),
    path('create-movie/', create_movie, name='create_movie'),
    path('movie-list/', movie_list, name='movie_list'),
    path('movie-details/<int:movie_id>/', movie_details, name='movie_details'),
    path('about-me/', about_me, name='about_me'),
    #endregion
    #region urls CBV
    path('edit-movie/<int:pk>/', MovieUpdateView.as_view(), name='edit_movie'),
    path('delete-movie/<int:pk>/', MovieDeleteView.as_view(), name='delete_movie'),
    #endregion
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
