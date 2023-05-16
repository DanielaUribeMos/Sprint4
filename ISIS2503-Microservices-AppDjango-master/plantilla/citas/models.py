from django.db import models

class Plantilla(models.Model):
    tipo = models.CharField(max_length=50)
    fecha = models.CharField(max_length=50)
    doctor = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.tipo)