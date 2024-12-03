from django.db import models

class productos(models.Model):
    perro = models.CharField(max_length=20)
    gato = models.CharField(max_length=20)
    caballo = models.BooleanField()
# Create your models here.

class Usuarios(models.Model):
    Nombre = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=50)

class posts(models.Model):
    image = models.ImageField(upload_to='images/')  # Directorio donde se almacenarán las imágenes
    caption = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    