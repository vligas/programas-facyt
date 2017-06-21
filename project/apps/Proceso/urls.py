from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [

    url(r'^$', login_required(views.home), name='home'),
    url(r'^crear_solicitud/$', login_required(views.crear_solicitud), name='crear_solicitud'),
    url(r'^solicitud/(?P<id>[0-9]+)/procesar/$', login_required(views.solicitud), name='solicitud'),
    url(r'^solicitud/(?P<id>[0-9]+)/confirmar_correo/$', login_required(views.recibido), name='confirmar_email'),
    url(r'^solicitud/(?P<id>[0-9]+)/descargar/$', login_required(views.descargar_programas), name='descargar_programas'),

]
