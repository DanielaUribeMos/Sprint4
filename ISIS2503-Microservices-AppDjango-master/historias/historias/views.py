from .models import Historia
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json
from django.db import connection

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

def busqueda(request):
    query = "SELECT * FROM historias_historia WHERE especializacion = %s"
    params = ['Cardiologia']
    
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        results = cursor.fetchall()
    
    respuesta = "Las historias de cardiología son: \n"

    for result in results:
        id_value=result[0]
        name_value=result[1]
        especializacion_value=result[2]
        costo_value=result[3]
        respuesta+= "Id: " + id_value + " Nombre: " + name_value + " Especialización: " + especializacion_value + " Costo: " + costo_value +" \n"

    respuesta = "Con un costo promedio de citas de: "
    query = "SELECT SUM(costo) FROM historias_historia WHERE especializacion = %s"

    with connection.cursor() as cursor:
        cursor.execute(query, params)
        results = cursor.fetchall()
    
    respuesta+= results

    return respuesta
