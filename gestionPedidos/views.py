from django.http import HttpResponse    
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

def busqueda_productos(request): ## primera Vista

    return render(request,"busqueda_productos.html")

def buscar(request):

    if request.GET["prd"]:

        #mensaje="Articulo buscado: %r" %request.GET["prd"]
        producto=request.GET["prd"]

        Articulos=Articulos.objects.filter(nombre_incontrains=producto)

    else:

        mensaje="No has introducido nada"    

    return HttpResponse(mensaje)