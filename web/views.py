from django.shortcuts import render, redirect
from .models import Portada , Devocional, Lider
from .forms import ContactoForm
from django.contrib import messages

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

def contacto(request):
    if request.method == 'POST':
        # Si alguien apretó "Enviar"
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            formulario.save() # ¡Guardado en la base de datos!
            messages.success(request, '¡Tu mensaje ha sido enviado! Te responderemos pronto.')
            return redirect('contacto') # Recargamos la página limpia
    else:
        # Si solo está entrando a ver la página
        formulario = ContactoForm()

    return render(request, 'contacto.html', {'formulario': formulario})

def donar(request):
    return render(request, 'donar.html')