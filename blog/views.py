import json
from django.http import JsonResponse
from django.core.serializers import serialize
from django.shortcuts import render
from .models import Entrada
from .models import Autor

def lista_entradas(request):
    entradas = Entrada.objects.all()
    return render(request, 'blog/lista_entradas.html', {'entradas': entradas})

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request,'blog/lista_autores.html',{'autores':autores})

def lista_resultado(request):
    autor = Autor.objects.get(nombre=request.POST.get('autor'))
    resultado = Entrada.objects.filter(autor=autor)
    return render(request,'blog/lista_resultado.html',{'resultado':resultado,'autor':autor.nombre})