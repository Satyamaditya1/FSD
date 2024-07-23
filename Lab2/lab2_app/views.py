from django.shortcuts import render
import datetime
from django.http import HttpResponse

def cdt(request):
    dt = datetime.datetime.now()
    resp = "<h1>Current Date and Time is %s </h1>"%(dt)
    return HttpResponse(resp)
