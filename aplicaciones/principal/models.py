from django.db import models
from decimal import Decimal, DecimalException
import datetime
import uuid
# Create your models here.

class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    evento = models.CharField(max_length=250)
    organizador = models.CharField(max_length=250)
    fecha = models.DateField( default=datetime.date.today, blank=True)
    telefono = models.CharField(max_length=13)
    # email = models.EmailField()
    medios = models.CharField(max_length=500, default="efectivo")
    meta = models.IntegerField(default=100000)
    costo = models.IntegerField(default=10000)
    direccion = models.CharField(max_length=300)
    ciudad = models.CharField(max_length=300, default="asuncion")
    image = models.FileField(blank=True)
    descripcion = models.CharField(max_length=10000)
    # random_url = models.UUIDField(default=uuid.uuid4)
    url = models.CharField(max_length=250, default="unidos-por-")
    beneficiario = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100, default="todos")
    # foto = models.ImageField(upload_to='eventos')
    latitud = models.DecimalField(max_digits=50, decimal_places=20, default=0)
    longitud = models.DecimalField(max_digits=50, decimal_places=20, default=0)
    
    def __str__(self):
        return self.evento
