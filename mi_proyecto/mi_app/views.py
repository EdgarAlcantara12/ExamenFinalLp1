from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Noticia, CategoriaHerramienta, Herramienta


@login_required
def index(request):
    return render(request, 'index.html')  

@login_required
def herramientas_detalle(request):
    categorias = CategoriaHerramienta.objects.prefetch_related('herramienta_set').all()
    return render(request, 'herramientas_detalle.html', {'categorias': categorias})


@login_required
def noticias(request):
    noticias = Noticia.objects.all().order_by('-fecha_publicacion')  # Ordenar por la fecha más reciente
    print(noticias)  # Agrega esto para verificar en la consola
    return render(request, 'noticias.html', {'noticias': noticias})

@login_required
def politicas_privacidad(request):
    return render(request, 'politicas_privacidad.html') 


@login_required
def contacto(request):
    return render(request, 'contacto.html')
