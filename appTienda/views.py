from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Pedido, Categoria
from .forms import PedidoForm
from django.urls import reverse
from django.db.models import Q

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

    return render(request, 'appTienda/seguimiento_pedido.html', {
        'pedido': pedido,
        'token': token,
        'url_seguimiento': url_seguimiento,
        'no_encontrado': False if pedido else True
    })
