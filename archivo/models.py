from django.db import models

# Create your models here.
class ArchivoExcel(models.Model):
    nombre = models.CharField(max_length=100)
    archivo = models.FileField(upload_to='archivos_excel/')

    def __str__(self):
        return self.nombre

