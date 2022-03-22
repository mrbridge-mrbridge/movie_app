from django.db.models import Q
from rest_framework.decorators import api_view

from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
#class Home(APIView):
#    """returns the Home page"""
#    def get(self, request, *args, **kwargs):
#        """renders home page"""
#        if request.user.is_authenticated:
#            return redirect('myprofiles')
#        return render(request, 'home.html')

class AllMovies(APIView):
    """
    returns all movies in database
    """
    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
class AllUsers(APIView):
    """
    returns all users in database
    """
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class UserCreate(APIView):
    """create a user"""
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ProfileCreate(APIView):
    """Create Profile Route"""
    def post(self, request):
        """
        POST Create profile information to endpoint
        /api/profile/create/
        """
        
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Watch(APIView):
    """Watch Video Route"""
    def get(self, request, pk):
        """
       GET request to get all videos with the PROFILE
        rating using the profile's uuid endpoint is
        /api/watch/<str:pk>/
        """
        profile = Profile.objects.get(uuid=pk)
        agelimit = profile.age_restriction
        movies = Movie.objects.get(age_restriction=agelimit)
        showcase = MovieSerializer(movies)
        return Response(showcase.data)


class ShowMovieDetail(APIView):
    """Show Specific Movie Details"""
    def get(self, request, movie_id):
        """
        GET request to get the particular movies information through
        the movies uuid endpoint is /api/movie/detail/<str:movie_id>/
        """
        try:

            movie = Movie.objects.get(uuid=movie_id)
            serializer = MovieSerializer(movie)

            return Response(serializer.data)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ShowMovie(APIView):
    """Show Movie Video """
    def get(self, request, movie_id):
        """
        GET request to get video url using the video's uuid
        endpoint is /api/movie/play/<str:movie_id>/
        """
        try:
            movies = Movie.objects.get(uuid=movie_id)
            serializer = MovieSerializer(movies)

            return Response(serializer.data["get_video"])
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
@api_view(['GET'])
def search_movie(request, pk):
    """search a movie"""
    query = pk
    
    if query:
        movies = Movie.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    else:
        return Response({"movies": []})