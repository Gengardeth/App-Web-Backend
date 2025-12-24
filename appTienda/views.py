from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.utils.safestring import mark_safe
import json
# Vista protegida de reporte
@login_required
def reporte(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    estado = request.GET.get('estado')
    filtros = {}
    if fecha_inicio:
        filtros['fecha_solicitada__gte'] = fecha_inicio
    if fecha_fin:
        filtros['fecha_solicitada__lte'] = fecha_fin
    if estado:
        filtros['estado_pedido'] = estado
    pedidos = Pedido.objects.filter(**filtros)
    # Gráfico: cantidad de pedidos por estado
    conteo = pedidos.values('estado_pedido').annotate(cantidad=Count('id')).order_by('estado_pedido')
    estados_dict = dict(Pedido.ESTADO_PEDIDO)
    grafico_labels = [estados_dict.get(c['estado_pedido'], c['estado_pedido']) for c in conteo]
    grafico_data = [c['cantidad'] for c in conteo]
    context = {
        'pedidos': pedidos,
        'estados': Pedido.ESTADO_PEDIDO,
        'grafico_labels': mark_safe(json.dumps(grafico_labels)),
        'grafico_data': mark_safe(json.dumps(grafico_data)),
    }
    return render(request, 'appTienda/reporte.html', context)
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Insumo, Pedido
from .serializers import InsumoSerializer, PedidoSerializer
from django.utils.dateparse import parse_date
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from django.db.models import Q as Q_drf

# API CRUD Insumos
class InsumoViewSet(viewsets.ModelViewSet):
    queryset = Insumo.objects.all()
    serializer_class = InsumoSerializer
    permission_classes = [permissions.AllowAny]

# API Crear/Modificar Pedidos (sin listar ni eliminar)
class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        return Response({'detail': 'Listar pedidos no permitido.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return Response({'detail': 'Eliminar pedidos no permitido.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# API Filtro de pedidos por parámetros
class PedidoFiltrarAPIView(APIView):
    def get(self, request):
        fecha_inicio = request.GET.get('fecha_inicio')
        fecha_fin = request.GET.get('fecha_fin')
        estados = request.GET.getlist('estados')
        max_resultados = request.GET.get('max_resultados')

        filtros = Q_drf()
        if fecha_inicio:
            try:
                fecha_inicio = parse_date(fecha_inicio)
                if not fecha_inicio:
                    raise ValueError
                filtros &= Q_drf(fecha_solicitada__gte=fecha_inicio)
            except Exception:
                return Response({'error': 'fecha_inicio inválida'}, status=400)
        if fecha_fin:
            try:
                fecha_fin = parse_date(fecha_fin)
                if not fecha_fin:
                    raise ValueError
                filtros &= Q_drf(fecha_solicitada__lte=fecha_fin)
            except Exception:
                return Response({'error': 'fecha_fin inválida'}, status=400)
        if estados:
            filtros &= Q_drf(estado_pedido__in=estados)
        pedidos = Pedido.objects.filter(filtros)
        if max_resultados:
            try:
                max_resultados = int(max_resultados)
                if max_resultados < 1 or max_resultados > 100:
                    raise ValueError
                pedidos = pedidos[:max_resultados]
            except Exception:
                return Response({'error': 'max_resultados inválido (1-100)'}, status=400)
        data = PedidoSerializer(pedidos, many=True).data
        return Response(data)
from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Pedido, Categoria
from .forms import PedidoForm
from django.urls import reverse
from django.db.models import Q
from django.contrib import messages
from django.utils import timezone


def catalogo(request):
    q = request.GET.get('q', '').strip()
    cat = request.GET.get('cat', '').strip()
    dest = request.GET.get('dest', '').strip()

    productos = Producto.objects.all()
    categorias = Categoria.objects.all()

    if q:
        productos = productos.filter(Q(nombre__icontains=q) | Q(descripcion__icontains=q))

    if cat:
        productos = productos.filter(categoria_id=cat)

    if dest == "1":
        productos = productos.filter(es_destacado=True)

    return render(request, 'appTienda/catalogo.html', {
        'productos': productos,
        'categorias': categorias,
        'q': q,
        'cat': cat,
        'dest': dest,
    })


def buscar_token(request):
    """Recibe un token (GET) y redirige a la vista pública de seguimiento."""
    token = request.GET.get('token', '').strip()

    if not token:
        messages.error(request, 'Ingresa un token para buscar tu pedido.')
        return redirect('catalogo')

    return redirect('seguimiento_pedido', token=token)


def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'appTienda/detalle_producto.html', {'producto': producto})


def pedir_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        form = PedidoForm(request.POST, request.FILES)
        if form.is_valid():
            p = form.save(commit=False)
            p.producto_referencia = producto
            p.plataforma = 'web'
            p.estado_pedido = 'solicitado'
            p.estado_pago = 'pendiente'
            p.save()
            return redirect('seguimiento_pedido', token=p.token_seguimiento)
    else:
        form = PedidoForm()

    return render(request, 'appTienda/pedido_form.html', {'form': form, 'producto': producto})


def seguimiento_pedido(request, token):
    pedido = Pedido.objects.filter(token_seguimiento=token).first()

    url_seguimiento = request.build_absolute_uri(
        reverse('seguimiento_pedido', args=[token])
    )

    hoy = timezone.localdate()
    atrasado = False
    if pedido and pedido.fecha_solicitada:
        if pedido.fecha_solicitada < hoy and pedido.estado_pedido not in ("finalizada", "cancelada"):
            atrasado = True

    return render(request, 'appTienda/seguimiento_pedido.html', {
        'pedido': pedido,
        'token': token,
        'url_seguimiento': url_seguimiento,
        'no_encontrado': False if pedido else True,
        'hoy': hoy,
        'atrasado': atrasado,
    })
