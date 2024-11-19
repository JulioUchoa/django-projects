from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'gastos/index.html')

def add_gastos(request):
    return render(request, 'gastos/add-gastos.html')