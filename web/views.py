from django.shortcuts import render
from .models import Portada , Devocional, Lider

# Create your views here.
def inicio(request):
    dato_portada = Portada.objects.filter(activa=True).last()
    lista_devocionales = Devocional.objects.order_by('-fecha')[:3]
    
    contexto = {
         'portada': dato_portada,
         'devocionales': lista_devocionales,
    }
    return render(request, 'index.html', contexto)

def lista_devocionales(request):
    todos_los_devos = Devocional.objects.order_by('-fecha')
    return render(request, 'devocionales.html', {'devocionales': todos_los_devos})

# web/views.py

def quienes_somos(request):
    # Traemos a los líderes ordenados por el número que le pongas (1, 2, 3...)
    lideres = Lider.objects.order_by('orden')
    return render(request, 'quienes_somos.html', {'lideres': lideres})