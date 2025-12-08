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


#commit 2:
@admin.register(Insumo)
class InsumoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tipo", "cantDisponible", "unidad", "marca", "color")
    list_filter = ("tipo", "marca", "color")
    search_fields = ("nombre", "marca")
    ordering = ("tipo", "nombre")
    list_per_page = 20


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre_cliente",
        "contacto",
        "plataforma",
        "estado_pedido",
        "estado_pago",
        "fecha_solicitada",
        "producto_referencia",
        "token_seguimiento",
    )
    list_filter = ("plataforma", "estado_pedido", "estado_pago", "fecha_solicitada")
    search_fields = ("nombre_cliente", "contacto", "token_seguimiento", "producto_referencia__nombre")
    date_hierarchy = "fecha_solicitada"
    readonly_fields = ("token_seguimiento",)
    ordering = ("-fecha_solicitada",)
    list_per_page = 20
