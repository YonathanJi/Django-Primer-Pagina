from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

def plantillanicial(request): ## primera Vista

    return render(request,"plantilla_base.html")

#########################

def otraplantilla(request): ## primera Vista

    return render(request,"plantilla1.html")
    