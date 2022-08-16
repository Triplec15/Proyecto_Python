from django.contrib import admin

from products.models import Products, Categoria, Contacto

# Register your models here.
admin.site.register(Products)
admin.site.register(Categoria)
admin.site.register(Contacto)