from django.shortcuts import render

# Create your views here.
def formulario(request):
    return render(request, 'formulario.html')
def index(request):
    return render (request, 'index.html')