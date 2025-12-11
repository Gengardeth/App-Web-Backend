from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nombre_cliente', 'contacto', 'descripcion', 'fecha_solicitada', 'foto_ref1', 'foto_ref2']
