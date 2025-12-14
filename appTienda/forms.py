from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ["nombre_cliente","contacto","descripcion","fecha_solicitada","foto_ref1","foto_ref2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if "nombre_cliente" in self.fields:
            self.fields["nombre_cliente"].widget = forms.TextInput(attrs={"class":"form-control","placeholder":"Nombre y apellido"})

        if "contacto" in self.fields:
            self.fields["contacto"].widget = forms.TextInput(attrs={"class":"form-control","placeholder":"+56 9 .... / correo / contacto"})

        if "descripcion" in self.fields:
            self.fields["descripcion"].widget = forms.Textarea(attrs={"class":"form-control","rows":"4","placeholder":"Describe tu pedido (medidas, color, detalles, etc.)"})

        if "fecha_solicitada" in self.fields:
            self.fields["fecha_solicitada"].widget = forms.DateInput(attrs={"class":"form-control","type":"date"})
            self.fields["fecha_solicitada"].required = False

        for f in ["foto_ref1","foto_ref2"]:
            if f in self.fields:
                self.fields[f].required = False

    def clean_contacto(self):
        c = (self.cleaned_data.get("contacto") or "").strip()
        if not c:
            raise ValidationError("Ingresa un contacto (teléfono o correo).")
        if len(c) < 6:
            raise ValidationError("El contacto es demasiado corto.")
        t = c.replace(" ","").replace("-","").replace("(","").replace(")","")
        if t.startswith("+"):
            t2 = t[1:]
        else:
            t2 = t
        if t2.isdigit() and len(t2) < 8:
            raise ValidationError("Teléfono demasiado corto.")
        return c

    def clean_descripcion(self):
        d = (self.cleaned_data.get("descripcion") or "").strip()
        if not d:
            raise ValidationError("Describe lo que necesitas.")
        if len(d) < 10:
            raise ValidationError("La descripción es muy corta.")
        return d

    def clean_fecha_solicitada(self):
        f = self.cleaned_data.get("fecha_solicitada")
        if not f:
            return f
        hoy = timezone.localdate()
        if f < hoy:
            raise ValidationError("La fecha solicitada no puede ser anterior a hoy.")
        return f
