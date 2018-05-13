from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pety/index.html')
def servicios(request):
    return render(request, 'pety/servicios.html')
def login(request):
    return render(request, 'pety/login.html')
def contacto(request):
    return render(request, 'pety/contacto.html')
def registrarse(request):
    return render(request, 'pety/registrarse.html')
