from django.urls import include, path
from .views import PeliculaViewSet, DirectorViewSet, GeneroViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"peliculas", PeliculaViewSet)
router.register(r"directores", DirectorViewSet)
router.register(r"generos", GeneroViewSet)

urlpatterns = [
    path('', include(router.urls)),
]