from .models import Historia
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json

def HistoriaList(request):
    queryset = Historia.objects.all()
    context = list(queryset.values('id', 'name', 'especializacion', 'costo'))
    return JsonResponse(context, safe=False)

def HistoriaCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        historia = Historia()
        historia.name = data_json["name"]
        historia.especializacion = data_json["especializacion"]
        historia.costo = data_json["costo"]
        historia.save()
        return HttpResponse("successfully created Historia")