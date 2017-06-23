from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [

    url(r'^$', login_required(views.home), name='home'),
    url(r'^crear_solicitud/$', login_required(views.crear_solicitud), name='crear_solicitud'),
    url(r'^solicitud/(?P<id>[0-9]+)/procesar/$', login_required(views.solicitud), name='solicitud'),
    url(r'^solicitud/(?P<id>[0-9]+)/descargar/$', login_required(views.descargar_programas), name='descargar_programas'),

    # ACCIONES
    url(r'^solicitud/(?P<id>[0-9]+)/confirmar_correo_recibido/$', login_required(views.recibido), name='confirmar_email_recibido'),
    url(r'^solicitud/(?P<id>[0-9]+)/confirmar_correo_procesado/$', login_required(views.procesado), name='confirmar_email_procesado'),
    url(r'^solicitud/(?P<id>[0-9]+)/confirmar_verificacion/$', login_required(views.verificado), name='confirmar_verificado'),
    url(r'^solicitud/(?P<id>[0-9]+)/confirmar_correo_firma/$', login_required(views.firma), name='confirmar_correo_firma'),
    url(r'^solicitud/(?P<id>[0-9]+)/confirmar_correo_listo/$', login_required(views.listo), name='confirmar_listo'),
    url(r'^solicitud/(?P<id>[0-9]+)/confirmar_entrega/$', login_required(views.entregado), name='confirmar_entregado'),

]
