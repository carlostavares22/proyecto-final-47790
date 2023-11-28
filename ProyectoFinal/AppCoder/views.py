from django.shortcuts import render
from django.http import HttpResponse

def start_view (request):
    return HttpResponse("Bienvenidos")


def courses_view (request):
    #return HttpResponse("Aquí mostraré los cursos")
    return render (request, 'AppCoder/father.html')
