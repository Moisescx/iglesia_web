from django.shortcuts import render
from .models import Portada , Devocional

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