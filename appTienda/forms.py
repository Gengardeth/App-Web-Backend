from django import forms
from django.core.exceptions import ValidationError
from .models import Pedido

def _has_field(model, name):
    try:
        model._meta.get_field(name)
        return True
    except:
        return False

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for c in ["nombre_cliente","telefono_cliente","direccion_entrega","cantidad"]:
            if c in self.fields:
                self.fields[c].widget.attrs.update({"class":"form-control"})

        if "nombre_cliente" in self.fields:
            self.fields["nombre_cliente"].widget.attrs.update({"placeholder":"Nombre y apellido"})

        if "telefono_cliente" in self.fields:
            self.fields["telefono_cliente"].widget.attrs.update({"placeholder":"+56 9 ...."})

        if "direccion_entrega" in self.fields:
            self.fields["direccion_entrega"].widget.attrs.update({"placeholder":"Dirección completa"})

        if "cantidad" in self.fields:
            self.fields["cantidad"].widget = forms.NumberInput(attrs={"class":"form-control","min":"1"})

        for x in ["producto_referencia","token_seguimiento","plataforma","estado_pedido","estado_pago","fecha_solicitud","created_at","updated_at"]:
            if x in self.fields:
                self.fields[x].required = False
                self.fields[x].widget = forms.HiddenInput()

    def clean(self):
        cleaned = super().clean()

        if "cantidad" in self.fields:
            cant = cleaned.get("cantidad")
            if cant is None:
                raise ValidationError("Ingresa una cantidad.")
            try:
                if int(cant) <= 0:
                    raise ValidationError("La cantidad debe ser mayor a 0.")
            except:
                raise ValidationError("Cantidad inválida.")

        if "telefono_cliente" in self.fields:
            tel = (cleaned.get("telefono_cliente") or "").strip()
            if tel:
                t = tel.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
                if t.startswith("+"):
                    t = t[1:]
                if not t.isdigit():
                    raise ValidationError("El teléfono debe contener solo números.")
                if len(t) < 8:
                    raise ValidationError("Teléfono demasiado corto.")

        if "direccion_entrega" in self.fields:
            dire = (cleaned.get("direccion_entrega") or "").strip()
            if dire and len(dire) < 6:
                raise ValidationError("La dirección es demasiado corta.")

        return cleaned

    def save(self, commit=True):
        obj = super().save(commit=False)

        if _has_field(Pedido, "plataforma"):
            obj.plataforma = getattr(obj, "plataforma", None)
        if _has_field(Pedido, "estado_pedido"):
            obj.estado_pedido = getattr(obj, "estado_pedido", None)
        if _has_field(Pedido, "estado_pago"):
            obj.estado_pago = getattr(obj, "estado_pago", None)

        if commit:
            obj.save()
        return obj
