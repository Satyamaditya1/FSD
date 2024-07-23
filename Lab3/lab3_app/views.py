from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def bcdt(request):
    dt = datetime.datetime.now() + datetime.timedelta(hours=-4)
    resp = "<html><head><title>Current Date and Time before by 4 hours</title></head><body><h1>Current Date and Time before by 4hrs is %s </h1></body></html>"%(dt)
    return HttpResponse(resp)

def acdt(request):
    dt = datetime.datetime.now() + datetime.timedelta(hours = 4)
    resp = "<html><head><title>Current Date and Time ahead by 4 hours</title></head><body><h1>Current Date and Time ahead by 4hrs is %s</h1></body></html>"%(dt)
    return HttpResponse(resp)
