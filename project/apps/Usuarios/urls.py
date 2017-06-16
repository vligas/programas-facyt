from django.contrib.auth.views import login
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^index/', views.index, name = 'index'),
    url(r'^login/', login, {'template_name':'login.html'}, name = 'login'),
]
