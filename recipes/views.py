from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Home')

def contato(request):
    return HttpResponse('Contato')

def Sobre(request):
    return HttpResponse('Sobre')