from django.db import models

class productos(models.Model):
    perro = models.CharField(max_length=20)
    gato = models.CharField(max_length=20)
    caballo = models.BooleanField()
# Create your models here.
