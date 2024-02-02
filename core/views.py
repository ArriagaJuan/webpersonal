from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def home(request):
    return render(request,'Portada.html')

def About(request):
    return render(request,'Acercademi.html')

def Portafolio(request):
    return render(request,'Portafolio.html')

def Contacto(request):
    return render(request,'Contacto.html')