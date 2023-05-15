from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
        url(r'^plantillas/$', plantillas),
]