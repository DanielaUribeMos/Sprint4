from .models import Plantilla
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json
import requests
from django.db import connection
from django.conf import settings

def PlantillaList(request):
    queryset = Plantilla.objects.all()
    context = list(queryset.values('id', 'tipo', 'fecha', 'doctor'))
    return JsonResponse(context, safe=False)

def PlantillaCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        plantilla = Plantilla()
        plantilla.tipo = data_json["tipo"]
        plantilla.fecha = data_json["fecha"]
        plantilla.doctor = data_json["doctor"]
        plantilla.save()
        return HttpResponse("successfully created Plantilla")
