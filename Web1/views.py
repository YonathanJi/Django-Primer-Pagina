from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

def saludo(request): ## primera Vista

    return render(request,"miplantilla.html")
    
    
#########################################################

def despedida(request): ## Despedida
    
    return HttpResponse("Adios")

##########################################################



def damefecha(request): ## Fecha y hora en tiempo real

    fecha_actual=datetime.datetime.now()

    documento = """<html>
    <body>
    <h2 style="text-align: center;">
    Fecha y hora Actuales %s
    </h2>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)


###########################################################


def calcularedad(request,edad, ano):

    #edadactual=18
    periodo=ano-2019
    edadfutura=edad+periodo
    documento="<html><body><h2>En el año %s tendrás %s años" %(ano, edadfutura)

    return HttpResponse(documento)
