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
from django.http import HttpResponseBadRequest

def PlantillaList(request):
    if request.method == 'GET':
        queryset = Plantilla.objects.all()
        context = list(queryset.values('id', 'tipo', 'fecha', 'doctor'))
        return JsonResponse(context, safe=False)
    
    return HttpResponseBadRequest("Invalid request method")
    

def PlantillaCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)

        if "tipo" not in data_json or not isinstance(data_json["tipo"], str):
            return HttpResponseBadRequest("Invalid 'tipo' value")
        if "fecha" not in data_json or not isinstance(data_json["fecha"], str):
            return HttpResponseBadRequest("Invalid 'fecha' value")
        if "doctor" not in data_json or not isinstance(data_json["doctor"], str):
            return HttpResponseBadRequest("Invalid 'doctor' value")
        
        plantilla = Plantilla()
        plantilla.tipo = data_json["tipo"]
        plantilla.fecha = data_json["fecha"]
        plantilla.doctor = data_json["doctor"]
        plantilla.save()
        return HttpResponse("successfully created Plantilla")

    return HttpResponseBadRequest("Invalid request method")
