from django.shortcuts import render, get_object_or_404
from .models import Fotografia



def index(request):
    fotografias = Fotografia.objects.all()

    return render(request, 'galeria/index.html',{"fotografias":fotografias})

def imagem(request, id):
    foto = get_object_or_404(Fotografia, id=id)

    return render(request, 'galeria/image.html', {"foto":foto})