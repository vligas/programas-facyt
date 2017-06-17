from django.shortcuts import render, redirect
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
