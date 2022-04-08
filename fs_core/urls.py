"""fs_core URL Configuration
"""
from django.urls import path, include
from fs_core import views


urlpatterns = [
    path('all-movies/', views.AllMovies.as_view(), name=""),
    path('profile/create/', views.ProfileCreate.as_view(), name=""),
    path('users/create/', views.UserCreate.as_view(), name=""),
    path('watch/<str:movie_id>/', views.ShowMovie.as_view(), name=""),
    path('all-movies/search/', views.search_movie, name=""),
    path('detail/<str:movie_id>', views.ShowMovieDetail.as_view(), name=""),
    path('all-movies/genre/<str:genre_name>', views.GenreMovie.as_view(), name="")
]