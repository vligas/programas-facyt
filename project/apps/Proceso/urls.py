from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^crear_solicitud/$', views.crear_solicitud, name='crear_solicitud'),
    url(r'^solicitud/(?P<id>[0-9]+)/procesar/$', views.solicitud, name='solicitud'),
    url(r'^solicitud/(?P<id>[0-9]+)/descargar/$', views.descargar_programas, name='descargar_programas'),
    url(r'^solicitud/(?P<solicitud_id>[0-9]+)/(?P<programa_id>[0-9]+)/$', views.eliminar_programa, name='eliminar_programa'),

    # ACCIONES
    url(r'^solicitud/(?P<id>[0-9]+)/confirmar_correo_recibido/$', views.recibido, name='confirmar_email_recibido'),
    url(r'^solicitud/(?P<id>[0-9]+)/confirmar_correo_procesado/$', views.procesado, name='confirmar_email_procesado'),
    url(r'^solicitud/(?P<id>[0-9]+)/confirmar_verificacion/$', views.verificado, name='confirmar_verificado'),
    url(r'^solicitud/(?P<id>[0-9]+)/confirmar_firma/$', views.firma, name='confirmar_firma'),
    url(r'^solicitud/(?P<id>[0-9]+)/confirmar_correo_listo/$', views.listo, name='confirmar_listo'),
    url(r'^solicitud/(?P<id>[0-9]+)/confirmar_entrega/$', views.entregado, name='confirmar_entregado'),

]
