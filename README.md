# App-Web-Backend

Proyecto Django para una aplicación web de tienda.

## Estructura del Proyecto

```
PRUEBA_3_GONZALOLUIS/
├── manage.py                      # Script de gestión de Django
├── PRUEBA_3_GONZALOLUIS/          # Configuración del proyecto
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── appTienda/                     # Aplicación principal
│   ├── migrations/
│   ├── templates/
│   │   └── appTienda/
│   │       └── base.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
└── .gitignore
```

## Cambios Realizados

### Commit Inicial
- ✅ Inicializado repositorio Git
- ✅ Agregado `.gitignore` con configuración para Django

### Cambios Posteriores
- ✅ Rama `main` subida a GitHub
- ✅ Creado README.md con documentación del proyecto
- ✅ Datos del cliente y medio de contacto.
- ✅ Plataforma de venta (por ejemplo: Instagram, WhatsApp, página web).
- ✅ Estado del pedido y estado del pago.
- ✅ Fecha solicitada por el cliente.
- ✅ Referencia al producto principal del pedido.
- ✅ `token_seguimiento` de solo lectura para rastrear el pedido sin     modificarlo manualmente.

Se configuró el admin para:

- ✅Mostrar columnas relevantes en las tablas de **Insumos** y **Pedidos**.
- ✅Filtrar por tipo, marca y color (Insumos).
- ✅Filtrar por plataforma, estado del pedido, estado del pago y fecha (Pedidos).
- ✅Buscar por nombre de cliente, contacto y token de seguimiento.
- ✅Ordenar registros y limitar la cantidad de filas por página,

## Requisitos
- Python 3.x
- Django
- Pillow

## Uso
Para ejecutar el servidor de desarrollo:
En el bash:

# Instalar Django
pip install django

# Install Pillow
pip install Pillow

# Aplicar migraciones
python manage.py migrate

# Crear superusuario para acceder al admin
python manage.py createsuperuser

# Levantar el servidor
python manage.py runserver

