from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
import json
from pymongo import MongoClient
import datetime
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.parsers import JSONParser
from bson.objectid import ObjectId

@api_view(["GET", "POST"])
def pacientes(request):
    client = MongoClient(settings.MONGO_CLI)
    db = client.widmy_db
    pacientes = db['pacientes']
    if request.method == "GET":
        result = []
        data = pacientes.find({})
        for dto in data:
            jsonData = {
                'id': str(dto['_id']),
                "nombre": dto['nombre'],
                'telefono': dto['etelefono'],
                'cedula': dto['cedula']
            }
            result.append(jsonData)
        client.close()
        return JsonResponse(result, safe=False)
    
    if request.method == 'POST':
        data = JSONParser().parse(request)
        result = pacientes.insert(data)
        respo ={
            "MongoObjectID": str(result),
            "Message": "nuevo objeto en la base de datos"
        }
        client.close()
        return JsonResponse(respo, safe=False)
