#segundo paso de la ruta de crear la api rest, ya definimos los modelos de la base de datos en models.py ahora serializamos los datos a json

from rest_framework import serializers  #traemos los serializers de rest framework, que es una libreria mas moderna para manjear api rest en django
from .models import Pelicula, Director, Genero #traemos los models de la base de datos para que aqui sean serializados a json

class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = ["id", "titulo", "portada", "release_year", "director", "generos"]

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ["id", "nombre", "birth_year", "nacionalidad"]

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ["id", "genero"]