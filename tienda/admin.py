from django.contrib import admin
from .models import Marca, Perfume, Variante

# Esto le dice a Django: "Por favor, permite administrar estos modelos"
admin.site.register(Marca)
admin.site.register(Perfume)
admin.site.register(Variante)