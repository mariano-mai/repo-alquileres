from django.db import models

# Create your models here.
class pago(models.Model):
    numero = models.IntegerField(blank=True, null=True)
    fecha_de_pago = models.DateField(blank=True, null=True)
    periodo_correspondiente = models.CharField(max_length=25)
    importe_alquiler = models.FloatField(max_length=10)
    importe_electricidad = models.FloatField(max_length=10)
    importe_agua = models.FloatField(max_length=10)
    pagado = models.BooleanField