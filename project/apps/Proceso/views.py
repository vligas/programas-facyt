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

    solicitud = get_object_or_404(models.Solicitud, pk=id)
    periodo, annio = cleaned_data.get('periodo').split('-')
    materias = cleaned_data.get('materias').split(',')
    materias = [ x.strip() for x in materias]
    result = ""

    programas = Programas.objects.filter(periodo_electivo = periodo, periodo_annio = annio)

    for programa in programas:
         if programa.codigo_materia in materia:
             result.append(programa)
             materias.remove(programa.codigo_materia)
             solicitud.programas.add(programa)


    return render(request,'solicitud.html', context)

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
