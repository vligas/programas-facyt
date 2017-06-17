from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.

def index(request):
    return HttpResponse("Hola")

def home(request):
    form = forms.SolicitudForm()
    return render(request, 'list.html', { 'form':form })

def solicitud(request):
    return render(request,'solicitud.html')

def crear_solicitud(request):
    return HttpResponse("Procesado")
