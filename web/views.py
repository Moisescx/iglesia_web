from django.shortcuts import render
from .models import Portada

# Create your views here.
def inicio(request):
    dato_portada = Portada.objects.filter(activa=True).last()
    contexto = {'portada': dato_portada}
    return render(request, 'index.html', contexto)