from django.contrib import admin
from .models import Evento, Emprendimiento
from decimal import Decimal, DecimalException

admin.site.register(Evento)
admin.site.register(Emprendimiento)
