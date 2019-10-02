from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
	return HttpResponse("<h1> Esta es mi página principal</h1>")

def about(request):
	return HttpResponse("<h1>Mi nombre es Mario</h1>")