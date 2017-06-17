from django.db import models
from django.contrib.auth.models import User #Necesario para el User de la relacion ForeignKey


# Create your models here.
ESTATUS_CHOICES = ( #Posibles estatus de la Solicitud
    ('R','Recibido'),
    ('E','Entregado'),
    ('P','En Proceso'),
)
# BUG DEBEN SER TUPLAS, NO LO ERAN


def path_solicitud(instance, filename): #Funcion loca que determina donde seran subidos los archivos y su formato
# file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'Solicitudes/{}_{}/{}'.format(instance.pk,instance.nombre.replace(' ','_'), filename)

class Solicitud(models.Model):
    nombre = models.CharField(max_length=50)#Nombre de la persona
    apellido = models.CharField(max_length=50)#Apellido de la persona
    cedula = models.CharField(max_length=15)#Cedula de la persona, es una cadena por: 'V.- 26.186.525'
    telefono = models.CharField(max_length=18)#Telefono de la persona, es una cadena por: '+58-414-582-5878'
    solvencia = models.BooleanField(default=True)#Solvencia por si la persona debe algo
    correo =  models.EmailField()#Correo de la persona
    archivo_adjunto = models.FileField(upload_to=path_solicitud)#Archivo ccon reporte de notas
    usuario_creador = models.ForeignKey(User, related_name="solicitudes_creadas")#Relacion con el Usuario ¿?¿?¿?¿?¿?
    usuario_procesador = models.ForeignKey(User, null=True, blank=True, related_name="solicitud_procesadas")#Relacion con el usuario ¿?¿?¿?

    # BUG AL TENER 2 FOREING KEY CON EL MISMO MODELO DABA ERROR, CAMBIE EL RELATED_NAME PARA SOLUCIONARLO

    fecha_creacion = models.DateTimeField(auto_now_add=True) #para que cuando se cree lo ponga automaticamente con la fecha actual
    fecha_firma = models.DateTimeField(null=True, blank=True)#null y blank son parametros para campos que no concoemos de primeras
    fecha_procesada = models.DateTimeField(null=True, blank=True)#Fecha al momento de procesar
    correo_recibido = models.BooleanField(default=False)#Logico que informa si el correo fue recibido
    correo_procesado = models.BooleanField(default=False)#logico que informa si el correo fue procesado
    estatus = models.CharField(default = 'R', choices=ESTATUS_CHOICES, max_length=10)#estatus actual de la Solicitud
    lista = models.FileField(upload_to=path_solicitud, null=True, blank=True)#Lista de programas de la persona

    def __str__(self):
        return self.nombre

# class Archivo(models.Model):
#     documento = FileField(upload_to='STRING')

    #def path_archivo(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    #return 'Solicitudes/{}_{}/{}'.format(instance.Solicitud.pk,instance.Solicitud.nombre.replace(' ','_'), filename)


class Programas(models.Model):
    codigo_materia =  models.CharField(max_length=15)# ejemplo: TAO-202
    periodo_electivo = models.CharField(max_length=10)# Estos 2 campos son para algo como
    periodo_annio = models.CharField(max_length=10)#por ejemplo: 1-2016
    #archivo = models.ForeignKey(Archivo)
