from django.db import models


class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    fuente = models.CharField(max_length=255, default="Desconocida")
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.titulo
    

class CategoriaHerramienta(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Herramienta(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    enlace = models.URLField(max_length=200, blank=True, null=True)
    categoria = models.ForeignKey(CategoriaHerramienta, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre  # Aquí se retorna el nombre de la herramienta
