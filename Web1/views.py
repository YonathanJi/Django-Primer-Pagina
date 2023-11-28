from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request): ## primera Vista

    doc_externo=open(r"C:\Users\pc\OneDrive - Universidad Santiago de Cali\5 - ProjectosDjango\Web1\Web1\plantillas\miplantilla.html")

    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context()

    documento=plt.render(ctx)

    return HttpResponse(documento)
    
    
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
