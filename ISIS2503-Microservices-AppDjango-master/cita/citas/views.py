from .models import Cita
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json
import requests
from django.db import connection
from django.conf import settings

def CitaList(request):
    queryset = Cita.objects.all()
    context = list(queryset.values('id', 'name', 'especializacion', 'costo'))
    return JsonResponse(context, safe=False)

def CitaCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        cita = Cita()
        cita.name = data_json["name"]
        cita.especializacion = data_json["especializacion"]
        cita.costo = data_json["costo"]
        cita.save()
        return HttpResponse("successfully created Cita")

def CitasCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        cita_list = []
        for cita_data in data_json:
            cita = Cita()
            cita.name = cita_data['name']
            cita.especializacion = cita_data['especializacion']
            cita.costo = cita_data['costo']
            cita_list.append(cita)
        Cita.objects.bulk_create(cita_list)
        return HttpResponse("successfully created Cita")


def dar_telefono(name):
    r = requests.get(settings.PATH_VAR, headers={"Accept":"application/json"})
    pacientes = r.json()
    for paciente in pacientes:
        if name == paciente["nombre"]:
            return paciente["telefono"]
    return ""


def busqueda(request):

    #Cardiologia
    query = "SELECT * FROM citas_cita WHERE especializacion = %s"
    params = ['Cardiologia']
    
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        results = cursor.fetchall()
    
    respuesta = "Las citas de cardiologia son: <br>"
    costos=0
    contador=0
    for result in results:
        id_value=result[0]
        name_value=result[1]
        especializacion_value=result[2]
        costo_value=result[3]
        respuesta+= "Id: " + str(id_value) + " Nombre: " + name_value + " Especializacion: " + especializacion_value + " Costo: " + str(costo_value) + " Telefono: " + dar_telefono(result[1]) + " <br>"
        costos+=costo_value
        contador+=1

    if len(results)>0:
        costo_promedio=costos/contador
        respuesta += "Con un costo promedio de citas de: " + str(costo_promedio) + "<br> <br>"
    else:
        respuesta += "No hay citas de esa categoria <br> <br>"

    #Neurologia
    query = "SELECT * FROM citas_cita WHERE especializacion = %s"
    params = ['Neurologia']
    
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        results = cursor.fetchall()
    
    respuesta += "Las citas de neurologia son: <br>"
    costos=0
    contador=0
    for result in results:
        id_value=result[0]
        name_value=result[1]
        especializacion_value=result[2]
        costo_value=result[3]
        respuesta+= "Id: " + str(id_value) + " Nombre: " + name_value + " Especializacion: " + especializacion_value + " Costo: " + str(costo_value) + "Telefono: " + dar_telefono(result[1]) + " <br>"
        costos+=costo_value
        contador+=1

    if len(results)>0:
        costo_promedio=costos/contador
        respuesta += "Con un costo promedio de citas de: " + str(costo_promedio) + "<br> <br>"
    else:
        respuesta += "No hay citas de esa categoria <br> <br>"

    #Neurologia
    query = "SELECT * FROM citas_cita WHERE especializacion = %s"
    params = ['Gastroentrelorogia']
    
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        results = cursor.fetchall()
    
    respuesta += "Las citas de gastroentrelorogia son: <br>"
    costos=0
    contador=0
    for result in results:
        id_value=result[0]
        name_value=result[1]
        especializacion_value=result[2]
        costo_value=result[3]
        respuesta+= "Id: " + str(id_value) + " Nombre: " + name_value + " Especializacion: " + especializacion_value + " Costo: " + str(costo_value) + "Telefono: " + dar_telefono(result[1]) + " <br>"
        costos+=costo_value
        contador+=1

    if len(results)>0:
        costo_promedio=costos/contador
        respuesta += "Con un costo promedio de citas de: " + str(costo_promedio) + "<br> <br>"
    else:
        respuesta += "No hay citas de esa categoria <br> <br>"

    return HttpResponse(respuesta)
