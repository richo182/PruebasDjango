from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def bienvenido(request):
    return HttpResponse('Hola mundo')


def despedirse(request):
    return HttpResponse('Adios mundo')


def contacto(request):
    return HttpResponse('Comuniquese a los siguientes numeros: 9999123456')
