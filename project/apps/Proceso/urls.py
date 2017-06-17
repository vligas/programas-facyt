from django.conf.urls import url

from . import views


urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^crear_solicitud/$', views.crear_solicitud, name='crear_solicitud'),
    url(r'^solicitud/$', views.solicitud, name='solicitud'),
]
