from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from . import models

# Create your views here.

def index(request):
    return HttpResponse("Hola")

def home(request):
    form = forms.SolicitudForm()
    solicitudes = models.Solicitud.objects.all()
    context={
        'form':form,
        'solicitudes':solicitudes,
    }
    return render(request, 'list.html', context)

def solicitud(request):
    return render(request,'solicitud.html')

def crear_solicitud(request):
    form = forms.SolicitudForm()
    if request.method == "POST":

        form = forms.SolicitudForm(request.POST, request.FILES)

        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.usuario_creador = request.user
            solicitud.save()
            return redirect('home')
        else:
            return HttpResponse("Algo salio mal")
    else:
        form = forms.SolicitudForm()
        return HttpResponse("Errorsito :(")
