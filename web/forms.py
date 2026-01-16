# web/forms.py
from django import forms
from .models import Mensaje

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['nombre', 'email', 'telefono', 'motivo', 'cuerpo']
        
        # Aquí le ponemos el maquillaje (Tailwind) a los campos feos de Django
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-lg bg-gray-50 dark:bg-gray-700 dark:text-gray-100 border border-gray-200 dark:border-gray-600 focus:border-blue-500 focus:bg-white dark:focus:bg-gray-700 focus:outline-none transition duration-200', 'placeholder': 'Tu nombre completo'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-3 rounded-lg bg-gray-50 dark:bg-gray-700 dark:text-gray-100 border border-gray-200 dark:border-gray-600 focus:border-blue-500 focus:bg-white dark:focus:bg-gray-700 focus:outline-none transition duration-200', 'placeholder': 'tucorreo@ejemplo.com'}),
            'telefono': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-lg bg-gray-50 dark:bg-gray-700 dark:text-gray-100 border border-gray-200 dark:border-gray-600 focus:border-blue-500 focus:bg-white dark:focus:bg-gray-700 focus:outline-none transition duration-200', 'placeholder': '+56 9 ...'}),
            'motivo': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-lg bg-gray-50 dark:bg-gray-700 dark:text-gray-100 border border-gray-200 dark:border-gray-600 focus:border-blue-500 focus:bg-white dark:focus:bg-gray-700 focus:outline-none transition duration-200', 'placeholder': 'Asunto del mensaje'}),
            'cuerpo': forms.Textarea(attrs={'class': 'w-full px-4 py-3 rounded-lg bg-gray-50 dark:bg-gray-700 dark:text-gray-100 border border-gray-200 dark:border-gray-600 focus:border-blue-500 focus:bg-white dark:focus:bg-gray-700 focus:outline-none transition duration-200 h-32', 'placeholder': 'Escribe tu mensaje aquí...'}),
        }
