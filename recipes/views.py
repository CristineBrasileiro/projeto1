from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html')


def sobre(request):
    return HttpResponse('SOBRE 1')


def contato(request):
    return HttpResponse('CONTATO 1')
