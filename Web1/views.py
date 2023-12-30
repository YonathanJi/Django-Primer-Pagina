from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

def inicio(request): ## primera Vista

    return render(request,"Amici.html")

def contacto_view(request): 

    return render(request,"Contactanos.html")

def simulador_view(request): 

    return render(request,"Simulador.html")