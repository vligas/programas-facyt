from django.contrib.auth.views import login
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', login, {'template_name':'login.html'}, name = 'login'),
    url(r'^index/', views.index, name = 'index'),
]
