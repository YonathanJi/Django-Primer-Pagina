from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

def amici(request): ## primera Vista

    return render(request,"Amici.html")
