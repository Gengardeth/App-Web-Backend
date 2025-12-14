from django.db import models
from django.core.exceptions import ValidationError
import uuid


class Categoria(models.Model):
    nombre = models.CharField(max_length=80)
    detalle = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    imagen1 = models.ImageField(upload_to='productos', blank=True, null=True)
    imagen2 = models.ImageField(upload_to='productos', blank=True, null=True)
    imagen3 = models.ImageField(upload_to='productos', blank=True, null=True)
    es_destacado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre


class Insumo(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=60)
    cantDisponible = models.IntegerField()
    unidad = models.CharField(max_length=20, blank=True, null=True)
    marca = models.CharField(max_length=60, blank=True, null=True)
    color = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    PLATAFORMAS = (
        ('fb', 'Facebook'),
        ('ig', 'Instagram'),
        ('wa', 'WhatsApp'),
        ('local', 'Presencial'),
        ('web', 'Sitio web'),
        ('otro', 'Otro')
    )

    ESTADO_PEDIDO = (
        ('solicitado', 'Solicitado'),
        ('aprobado', 'Aprobado'),
        ('proceso', 'En proceso'),
        ('realizada', 'Realizada'),
        ('entregada', 'Entregada'),
        ('finalizada', 'Finalizada'),
        ('cancelada', 'Cancelada')
    )

    ESTADO_PAGO = (
        ('pendiente', 'Pendiente'),
        ('parcial', 'Parcial'),
        ('pagado', 'Pagado')
    )

    nombre_cliente = models.CharField(max_length=150)
    contacto = models.CharField(max_length=150)
    producto_referencia = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, blank=True)
    descripcion = models.TextField()
    plataforma = models.CharField(max_length=20, choices=PLATAFORMAS, default='web')
    fecha_solicitada = models.DateField(null=True, blank=True)
    estado_pedido = models.CharField(max_length=20, choices=ESTADO_PEDIDO, default='solicitado')
    estado_pago = models.CharField(max_length=20, choices=ESTADO_PAGO, default='pendiente')
    token_seguimiento = models.CharField(max_length=20, unique=True, blank=True)
    foto_ref1 = models.ImageField(upload_to='pedidos', blank=True, null=True)
    foto_ref2 = models.ImageField(upload_to='pedidos', blank=True, null=True)

    # --------- Validaciones lucho ---------

    def clean(self):
        if self.estado_pedido == 'finalizada' and self.estado_pago != 'pagado':
            raise ValidationError(
                "No puedes marcar el pedido como 'Listo' si el pago no está Realizado."
            )

    def save(self, *args, **kwargs):
        if not self.token_seguimiento:
            self.token_seguimiento = uuid.uuid4().hex[:10]

        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre_cliente
