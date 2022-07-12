from django.contrib import admin
from .models import Categoria, Producto
# Register your models here.

admin.site.register(Producto)
admin.site.register(Categoria)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')