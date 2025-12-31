from django.db import models

class Portada(models.Model):
    titulo = models.CharField(max_length=200, help_text="El título grande (Ej: Bienvenidos)")
    subtitulo = models.TextField(help_text="El texto pequeño de abajo")
    imagen = models.ImageField(upload_to='portadas/', blank=True, null=True, help_text="Imagen de fondo")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activa = models.BooleanField(default=True, help_text="Marca esta casilla si quieres que esta sea la portada actual")

    def __str__(self):
        return self.titulo

class Devocional(models.Model):
    titulo = models.CharField(max_length=200, help_text="Ej: La Paz de Dios")
    
    # Aquí damos crédito a la hermana que lo grabó
    autora = models.CharField(max_length=100, help_text="Ej: Hermana María") 
    
    fecha = models.DateField(auto_now_add=True)
    
    # Aquí pegaremos el link (de Youtube o el embed de Facebook)
    video_link = models.URLField(help_text="El link del video (YouTube o Facebook)")
    
    descripcion = models.TextField(blank=True, null=True, help_text="Breve resumen")
    
    def get_embed_url(self):
        """Versión blindada para Facebook y YouTube Shorts"""
        url = self.video_link
        
        if not url:
            return ""

        # --- CASO 1: YOUTUBE ---
        if "youtu" in url:
            # Primero quitamos cualquier cosa extra después del signo de pregunta (?)
            # Ejemplo: .../shorts/abcde?feature=share  -> .../shorts/abcde
            url_limpia = url.split("?")[0]

            if "shorts/" in url_limpia:
                return url_limpia.replace("shorts/", "embed/")
            
            if "watch?v=" in url_limpia:
                return url_limpia.replace("watch?v=", "embed/")
            
            if "youtu.be/" in url_limpia:
                return url_limpia.replace("youtu.be/", "www.youtube.com/embed/")

        # --- CASO 2: FACEBOOK (La prioridad) ---
        elif "facebook.com" in url or "fb.watch" in url:
            # Importante: Facebook necesita que el link esté "codificado"
            from urllib.parse import quote
            
            # Si el link es de móvil (m.facebook), lo pasamos a www para evitar errores
            url = url.replace("m.facebook.com", "www.facebook.com")
            
            encoded_url = quote(url)
            # Usamos el plugin oficial de video de Facebook
            return f"https://www.facebook.com/plugins/video.php?href={encoded_url}&show_text=0&width=560"
            
        # Si no es ninguno, devolvemos el original
        return url