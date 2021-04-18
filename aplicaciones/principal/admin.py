from django.contrib import admin
from .models import Evento
from decimal import Decimal, DecimalException

admin.site.register(Evento)
