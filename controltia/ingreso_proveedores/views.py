from django.shortcuts import render
import json
from django.http import HttpResponse
from django.conf import settings
import datetime
from .models import Reunion, Historial
import pytz
from django.contrib.auth import authenticate, login
# Create your views here.
import requests
from django.shortcuts import redirect

def get_reunion(request):

    content = {}

    content["status"] = 0
    content["message"] = ""

    if request.method == 'GET':

        try:
            reunion_id = request.GET["cod"]
        except:
            content["message"] = "Parámetros no válidos"
            json_data = json.dumps(content)
            return HttpResponse(json_data, content_type="application/json")

        try:
            reunion = Reunion.objects.get(id=reunion_id)
        except:
            content["message"] = "No hemos podido encontrar la reunión #" + str(reunion_id) + ", contactarse con el administrador."
            json_data = json.dumps(content)
            return HttpResponse(json_data, content_type="application/json")

        reunion_horario = (reunion.horario - datetime.timedelta(hours=5)).replace(tzinfo=None)

        if (reunion_horario <= (datetime.datetime.now() + datetime.timedelta(minutes=10)).replace(tzinfo=None)) and (reunion_horario >= (datetime.datetime.now() - datetime.timedelta(minutes=10)).replace(tzinfo=None)):
            if reunion.activa == True:
                content["status"] = 1
                content["message"] = "Estimado(a) " + reunion.nombre + ", su reunión es en la sala " + reunion.sala.nombre + "."
                post_historial(reunion, True, content["message"])
                json_data = json.dumps(content)
                return HttpResponse(json_data, content_type="application/json")
            else:
                content["message"] = "Estimado(a) " + reunion.nombre + ", su reunión no esta activa."
                post_historial(reunion, False, content["message"])
                json_data = json.dumps(content)
                return HttpResponse(json_data, content_type="application/json")
        else:
            content["message"] = "Estimado(a) " + reunion.nombre + ", esta ingresando fuera del horario de ingreso permitido."
            post_historial(reunion, False, content["message"])
            json_data = json.dumps(content)
            return HttpResponse(json_data, content_type="application/json")

    else:
        content["message"] = "Método no válido."
        json_data = json.dumps(content)
        return HttpResponse(json_data, content_type="application/json")


def post_historial(reunion, ingreso, detalle):
    historial = Historial(reunion=reunion, ingreso=ingreso, detalle=detalle, create_at=datetime.datetime.now())
    historial.save()



def autologin(request):
    if request.method == 'GET':

        #username = request.GET["username"]
        #password = request.GET["password"]

        user = authenticate(username="tia", password="datascience")
        if user is not None:
            login(request, user)
            return redirect('/admin/')
        else:
            return redirect('/admin/')
