from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hola")

def home(request):
    return render(request, 'list.html')

def solicitud(request):
    return render(request,'solicitud.html')
