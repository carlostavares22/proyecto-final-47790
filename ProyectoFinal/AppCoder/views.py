from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

def start_view (request):
    return HttpResponse("Bienvenidos")

def old_courses_view (request):
    #return HttpResponse("Aquí mostraré los cursos")
    return render (request, 'AppCoder/father.html')


def courses_view (request):
    nombre = "Carlos"
    apellido = "Tavares"
    diccionario = {'nombre': nombre, 'apellido': apellido, 'nacionalidad': 'Dominicano'}

    ruta = "D:/carlo/Proyecto_Final-Tavares/ProyectoFinal/AppCoder/templates/AppCoder/father.html"
    mi_archivo = open(ruta, "r")

    plantilla = Template(mi_archivo.read()) # Carga el documento en memmoria
    contexto = Context(diccionario)
    documento = plantilla.render(contexto)

    return HttpResponse (documento)