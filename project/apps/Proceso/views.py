from django.shortcuts import render, redirect, get_object_or_404
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

def solicitud(request, id):

    form = forms.ProcesarForm(request.POST)
    if form.is_valid():
        solocitud = form.save(commit=False)
        return HttpResponse("Hola")

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

def recibido(request, id):
    solicitud = get_object_or_404(models.Solicitud, pk=id)
    solicitud.correo_recibido = True
    solicitud.save()
    return redirect('home')
