from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Pedido
from .forms import PedidoForm

def catalogo(request):
    productos = Producto.objects.all()
    return render(request, 'appTienda/catalogo.html', {'productos': productos})

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
    return render(request, 'appTienda/seguimiento_pedido.html', {'pedido': pedido})
