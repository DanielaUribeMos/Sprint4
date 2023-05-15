from django.db import models

class Historia(models.Model):
    name = models.CharField(max_length=50)
    especializacion = models.CharField(max_length=50)
    costo = models.IntegerField(null=False, default=None)

    def __str__(self):
        return '{}'.format(self.name)