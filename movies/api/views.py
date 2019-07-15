from django_filters.rest_framework import DjangoFilterBackend
from movies.models import Movie
from movies.api.serializers import MovieCreateSerializer
from movies.api.serializers import MovieSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly


class MovieListAPIView(generics.ListAPIView):
    """
    get:
    Return a list of all the existing movies.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailAPIView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieCreateAPIView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieCreateSerializer
    permission_classes = [IsAuthenticated]


class MovieUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieCreateSerializer
    permission_classes = [IsOwnerOrReadOnly]


class MovieDeleteAPIView(generics.DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsOwnerOrReadOnly]
