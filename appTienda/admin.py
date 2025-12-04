from django.contrib import admin
from .models import Categoria, Producto, Insumo, Pedido


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "detalle")
    search_fields = ("nombre",)
    ordering = ("nombre",)
    list_per_page = 20


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio_base", "es_destacado")
    list_filter = ("categoria", "es_destacado")
    search_fields = ("nombre", "categoria__nombre")
    ordering = ("categoria", "nombre")
    list_per_page = 20


