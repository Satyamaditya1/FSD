from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def contactus(request):
    return render(request, 'contactus.html')

def aboutus(request):
    return render(request, 'about.html')
# Create your views here.
