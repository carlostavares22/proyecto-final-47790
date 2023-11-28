from django.urls import path
from django.http import HttpResponse

def view_inicio(request):
    return HttpResponse("Bienvenidos")

def view_cursos(request):
    return HttpResponse("Aquí mostraré los cursos")

urlpatterns = [
    path('inicio/', view_inicio),
    path('cursos/', view_cursos)
]
