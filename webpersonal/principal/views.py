from django.shortcuts import render, HttpResponse
from .models import Proyecto

# Create your views here.
def home(request):
	return render(request, 'principal/home.html')

def about(request):
	return render(request, 'principal/about.html')

def contacto(request):
	return render(request, 'principal/contacto.html')

def portafolio(request):
	lista = Proyecto.objects.all()
	contexto = {'lista': lista}
	return render(request, 'principal/portafolio.html', contexto)