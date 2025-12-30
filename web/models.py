from django.db import models

class Portada(models.Model):
    titulo = models.CharField(max_length=200, help_text="El título grande (Ej: Bienvenidos)")
    subtitulo = models.TextField(help_text="El texto pequeño de abajo")
    imagen = models.ImageField(upload_to='portadas/', blank=True, null=True, help_text="Imagen de fondo")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activa = models.BooleanField(default=True, help_text="Marca esta casilla si quieres que esta sea la portada actual")

    def __str__(self):
        return self.titulo