from django.urls import path
from django.http import HttpResponse
from AppCoder.views import start_view,courses_view

urlpatterns = [
    path('inicio/', start_view),
    path('cursos/', courses_view)
]
