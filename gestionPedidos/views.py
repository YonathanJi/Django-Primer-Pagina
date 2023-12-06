from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

def busqueda_productos(request): ## primera Vista

    return render(request,"busqueda_productos.html")