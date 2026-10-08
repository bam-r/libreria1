from rest_framework import viewsets  #importamos de drf la funcion para hacer las views actualizadas y simplificadas
from .models import Pelicula, Director, Genero
from .serializers import PeliculaSerializer, DirectorSerializer, GeneroSerializer

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()

    serializer_class= DirectorSerializer

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()

    serializer_class= GeneroSerializer

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()

    serializer_class= PeliculaSerializer