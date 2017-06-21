from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.conf import settings

from io import BytesIO
import os
import zipfile

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
    form = forms.ProcesarForm()

    if request.method == "POST":
        form = forms.ProcesarForm(request.POST)

        if form.is_valid():
            periodo, annio = form.cleaned_data.get('periodo').split('-')
            materias = form.cleaned_data.get('materias').split(',')
            materias = [ x.strip() for x in materias]
            result = []

            programas = models.Programas.objects.filter(periodo_electivo = periodo, periodo_annio = annio)

            if programas:
                for programa in programas:
                     if programa.codigo_materia in materias:
                         result.append(programa)
                         materias.remove(programa.codigo_materia)
                         solicitud.programas.add(programa)

                for materia in materias:
                    form.add_error(None, 'La materia "{}" no concuerda con el periodo {}-{}'.format(materia, periodo, annio))
            else:
                form.add_error('periodo', 'No existe el periodo {}-{}'.format(periodo,annio))

    context = {
        'form' : form,
        'solicitud' : solicitud,
    }


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



def descargar_programas(request, id):

    solicitud = get_object_or_404(models.Solicitud, pk=id)
    programas = solicitud.programas.all()
    result = BytesIO()
    filenames = []

    for x in programas:
        filenames.append(os.path.join(settings.BASE_DIR, x.archivo.documento.url.lstrip('/')))

    print(settings.BASE_DIR)

    # Folder name in ZIP archive which contains the above files
    # E.g [thearchive.zip]/somefiles/file2.txt
    zip_subdir = "programas"
    zip_filename = "{}_{}_{}.zip".format(solicitud.pk,solicitud.nombre,solicitud.apellido)


    # The zip compressor
    zf = zipfile.ZipFile(result, "w")

    for fpath in filenames:
        # Calculate path for file in zip
        fdir, fname = os.path.split(fpath)
        zip_path = os.path.join(zip_subdir, fname)

        # Add file, at correct path
        zf.write(fpath, zip_path)

    # Must close zip for all contents to be written
    zf.close()

    # Grab ZIP file from in-memory, make response with correct MIME-type
    resp = HttpResponse(result.getvalue(), content_type = "application/x-zip-compressed")
    # ..and correct content-disposition
    resp['Content-Disposition'] = 'attachment; filename={}'.format(zip_filename)
    resp['Content-length'] = result.tell()

    return resp
