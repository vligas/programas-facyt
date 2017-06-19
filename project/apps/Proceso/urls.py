from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [

    url(r'^$', login_required(views.home), name='home'),
    url(r'^crear_solicitud/$', login_required(views.crear_solicitud), name='crear_solicitud'),
    url(r'^solicitud/$', login_required(views.solicitud), name='solicitud'),
    url(r'^(?P<id>[0-9]+)/$', login_required(views.recibido), name='confirmar_email'),
]
