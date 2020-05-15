from django.contrib import admin
from .models import Cliente, Consumidor, Pedido

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Consumidor)
admin.site.register(Pedido)
