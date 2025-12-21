from django.contrib import admin, messages
from django.utils import timezone
from django.utils.html import format_html
from django.db.models import Q

from .models import Categoria, Producto, Insumo, Pedido


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "detalle")
    search_fields = ("nombre",)
    ordering = ("nombre",)
    list_per_page = 20


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("miniatura", "nombre", "categoria", "precio_base", "es_destacado")
    list_filter = ("categoria", "es_destacado")
    search_fields = ("nombre", "categoria__nombre")
    ordering = ("categoria", "nombre")
    list_per_page = 20
    save_on_top = True
    save_as = True

    def miniatura(self, obj):
        img = obj.imagen1 or obj.imagen2 or obj.imagen3
        if img and hasattr(img, "url"):
            return format_html(
                '<img src="{}" style="width:60px;height:60px;object-fit:cover;border-radius:8px;" />',
                img.url,
            )
        return "—"
    miniatura.short_description = "Img"



@admin.register(Insumo)
class InsumoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tipo", "cantDisponible", "unidad", "marca", "color")
    list_filter = ("tipo", "marca", "color")
    search_fields = ("nombre", "marca")
    ordering = ("tipo", "nombre")
    list_per_page = 20



class AtrasadosFilter(admin.SimpleListFilter):
    title = "Atrasados"
    parameter_name = "atrasado"

    def lookups(self, request, model_admin):
        return (
            ("1", "Solo atrasados"),
            ("0", "No atrasados"),
        )

    def queryset(self, request, queryset):
        hoy = timezone.localdate()
        estados_cerrados = ["finalizada", "cancelada"]

        if self.value() == "1":
            return (
                queryset
                .filter(fecha_solicitada__lt=hoy)
                .exclude(estado_pedido__in=estados_cerrados)
            )

        if self.value() == "0":
            return queryset.filter(
                Q(fecha_solicitada__gte=hoy) |
                Q(estado_pedido__in=estados_cerrados) |
                Q(fecha_solicitada__isnull=True)
            )

        return queryset


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre_cliente",
        "contacto",
        "plataforma",
        "estado_badge",
        "pago_badge",
        "fecha_solicitada",
        "producto_referencia",
        "token_seguimiento",
    )

    
    list_filter = ("plataforma", "estado_pedido", "estado_pago", "fecha_solicitada", AtrasadosFilter)
    search_fields = ("nombre_cliente", "contacto", "token_seguimiento", "producto_referencia__nombre")
    date_hierarchy = "fecha_solicitada"
    readonly_fields = ("token_seguimiento",)
    ordering = ("-fecha_solicitada",)
    list_per_page = 20
    save_on_top = True
    save_as = True
    
    actions = ("marcar_pagado", "pasar_a_proceso", "marcar_finalizada_si_pagado")

    def estado_badge(self, obj):
        colores = {
            "solicitado": "#6c757d",
            "aprobado": "#0d6efd",
            "proceso": "#fd7e14",
            "realizada": "#20c997",
            "entregada": "#198754",
            "finalizada": "#0f5132",
            "cancelada": "#dc3545",
        }
        color = colores.get(obj.estado_pedido, "#6c757d")
        label = obj.get_estado_pedido_display()
        return format_html(
            '<span style="padding:2px 10px;border-radius:999px;color:white;background:{};font-size:12px;">{}</span>',
            color, label
        )
    estado_badge.short_description = "Estado"

    def pago_badge(self, obj):
        colores = {
            "pendiente": "#dc3545",
            "parcial": "#fd7e14",
            "pagado": "#198754",
        }
        color = colores.get(obj.estado_pago, "#6c757d")
        label = obj.get_estado_pago_display()
        return format_html(
            '<span style="padding:2px 10px;border-radius:999px;color:white;background:{};font-size:12px;">{}</span>',
            color, label
        )
    pago_badge.short_description = "Pago"

    
    @admin.action(description="Marcar como PAGADO")
    def marcar_pagado(self, request, queryset):
        updated = queryset.update(estado_pago="pagado")
        self.message_user(request, f"{updated} pedido(s) marcados como Pagado.", level=messages.SUCCESS)

    @admin.action(description="Pasar a EN PROCESO")
    def pasar_a_proceso(self, request, queryset):
        updated = queryset.update(estado_pedido="proceso")
        self.message_user(request, f"{updated} pedido(s) pasados a En proceso.", level=messages.SUCCESS)

    @admin.action(description="Marcar como FINALIZADA (solo si está Pagado)")
    def marcar_finalizada_si_pagado(self, request, queryset):
        qs_ok = queryset.filter(estado_pago="pagado")
        qs_no = queryset.exclude(estado_pago="pagado")

        ok = qs_ok.update(estado_pedido="finalizada")
        no = qs_no.count()

        if ok:
            self.message_user(request, f"{ok} pedido(s) finalizados correctamente.", level=messages.SUCCESS)
        if no:
            self.message_user(
                request,
                f"{no} pedido(s) NO se finalizaron porque el pago no está Pagado.",
                level=messages.WARNING
            )