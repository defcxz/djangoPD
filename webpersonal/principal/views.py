from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
	return render(request, 'templates/home.html')

def about(request):
	return render(request, 'templates/about.html')

def contacto(request):
	return render(request, 'templates/contacto.html')

def portafolio(request):
	return render(request, 'templates/portafolio.html')