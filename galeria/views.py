from django.shortcuts import render, get_object_or_404
from .models import Fotografia



def index(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicado=True)

    return render(request, 'galeria/index.html',{"fotografias":fotografias})

def imagem(request, id):
    foto = get_object_or_404(Fotografia, id=id)

    return render(request, 'galeria/image.html', {"foto":foto})

def buscar(request):
    fotos = Fotografia.objects.order_by("data_fotografia").filter(publicado=True)
    nome_buscar = request.GET['buscar']
    if nome_buscar:
       filtrada = fotos.filter(name_icontains = nome_buscar)
    return render(request, "galeria/buscar.html",{"fotografias":filtrada})