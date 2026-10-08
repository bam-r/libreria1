#primer paso para constuir una api rest, definimos los modelos que migraremos a la base de datos

from django.db import models

class Director(models.Model):
    nombre = models.CharField(max_length=50, unique = True)
    birth_year = models.IntegerField()
    nacionalidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    genero = models.CharField(max_length=50, unique = True)

    def __str__(self):
        return self.genero

class Pelicula(models.Model):
    titulo = models.CharField(max_length=50, unique = True)
    portada = models.URLField()
    release_year = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    generos = models.ManyToManyField(Genero)

    def __str__(self):
        return self.titulo

