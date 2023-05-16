from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^plantillas/', views.PlantillaList, name='plantillaList'),
    url(r'^plantilacreate/$', csrf_exempt(views.PlantillaCreate), name='plantillaCreate'),
]