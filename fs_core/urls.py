"""fs_core URL Configuration
"""
from django.urls import path, include
from fs_core import views


urlpatterns = [
    path('all-movies/', views.AllMovies.as_view(), name=""),
    path('users/', views.AllUsers.as_view(), name=""),
    path('profile/create/', views.ProfileCreate.as_view(), name=""),
    path('user/create/', views.ProfileCreate.as_view(), name=""),
    path('watch/<str:movie_id>/', views.ShowMovie.as_view(), name=""),
    path('all-movies/search/<str:pk>', views.search_movie, name=""),
]