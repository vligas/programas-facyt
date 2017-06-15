from django.db import models
from django.contrib.auth.models import User


# Create your models here.
OPCIONES_ESTATUS = (
    ('Recibido'),
    ('Entregado'),
    ('En Proceso'),
)

class Solicitud(models.Model):
    nombre = models.CharField(max_length=200)
    cedula = models.IntegerField()
    telefono = models.CharField(_('Telefono'), max_length=18)
    solvencia = models.BooleanField()
    archivo_adjunto = FileField(upload_to='path_solicitud')
    usuario_creador = models.ForeignKey(User)
    usuario_procesador = models.ForeignKey(User)
    fecha_creacion = models.DateTimeField()
    fecha_firma = models.DateTimeField()
    correo_recibido = models.BooleanField()
    correo_procesado = models.BooleanField()
    estatus =

    def __str__(self):
        return self.nombre

    def path_solicitud(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'Solicitudes/{}_{}/{}'.format(instance.Solicitud.pk,instance.Solicitud.nombre.replace(' ','_'), filename)

class Programas(models.Model):
    codigo_materia =  models.CharField()
    periodo = models.CharField()
    archivo =
