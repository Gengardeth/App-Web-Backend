# App-Web-Backend

Aplicación web Django para gestionar una tienda en línea con seguimiento de pedidos, gestión de insumos y administración de clientes.

## 📋 Descripción

Sistema de gestión de tienda que permite:
- 📦 Registrar y dar seguimiento a pedidos
- 🏪 Gestionar insumos y productos
- 👥 Administrar datos de clientes
- 🔍 Rastrear pedidos con token único
- 💾 Interfaz de administración completa
- 🛍️ Catálogo público de productos con búsqueda y filtros (Commit 4)
- 🔗 Mostrar token y URL de seguimiento al cliente + mejoras de validación/token (Commit 5)
- 📂 Modelo de Categorías y Productos mejorado + vistas del catálogo (Commit 6)

## 📁 Estructura del Proyecto

```
├── manage.py # Script de gestión de Django
├── README.md # Este archivo
├── PRUEBA_3_GONZALOLUIS/ # Configuración del proyecto
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── appTienda/ # Aplicación principal
│ ├── migrations/ # Migraciones de base de datos
│ ├── static/
│ │ └── css/
│ │ └── styles.css # Estilos del catálogo y productos
│ ├── templates/
│ │ └── appTienda/
│ │ ├── base.html # Template base
│ │ ├── catalogo.html # Catálogo con búsqueda y filtros
│ │ ├── detalle_producto.html # Página detalle de producto
│ │ ├── pedido_form.html # Formulario para crear pedidos
│ │ └── seguimiento_pedido.html # Seguimiento con token y URL
│ ├── init.py
│ ├── admin.py # Configuración de administrador
│ ├── apps.py
│ ├── forms.py # Formulario Pedido con widgets (Bootstrap)
│ ├── models.py # Modelos: Categoría, Producto, Insumo, Pedido, etc.
│ ├── urls.py # Rutas de la app
│ ├── tests.py
│ └── views.py # Vistas: catálogo, detalle, crear pedido, seguimiento
└── .gitignore
```

## ✨ Características Implementadas

### Modelos de Datos
- **Categorías**: Categorización de productos con nombre y detalle
- **Productos**: Información detallada con múltiples imágenes, precio y estado de destacado
- **Clientes**: Datos personales, contacto y plataforma de comunicación
- **Insumos/Productos**: Tipo, marca, color e información de disponibilidad
- **Pedidos**: Estado del pedido, estado del pago, fecha solicitada y referencias
- **Token de Seguimiento**: Identificador único para rastrear pedidos sin modificación manual

### Panel de Administración
- ✅ Visualización optimizada con columnas relevantes
- ✅ Filtros avanzados:
  - Por tipo, marca y color (Insumos)
  - Por plataforma, estado de pedido, estado de pago y fecha (Pedidos)
- ✅ Búsqueda por nombre de cliente, contacto y token de seguimiento
- ✅ Ordenamiento y paginación de registros

### Templates
- ✅ Template base HTML para la aplicación
- ✅ Catálogo con filtros/búsqueda y paginación
- ✅ Detalle de producto con múltiples imágenes
- ✅ Formulario de pedido con validación
- ✅ Página de seguimiento (con token y URL de seguimiento)

### Vistas y Funcionalidades (Commit 6)
- **catalogo()**: Listado de productos con búsqueda por nombre/descripción, filtrado por categoría y estado destacado
- **detalle_producto()**: Visualización detallada de un producto con imágenes
- **pedir_producto()**: Formulario para realizar pedidos de productos específicos
- **seguimiento_pedido()**: Rastrear pedido por token único con URL compartible

## 🛠️ Requisitos

- Python 3.8+
- Django 4.0+
- Pillow (para procesamiento de imágenes)
- ✅Buscar por nombre de cliente, contacto y token de seguimiento.
- ✅Ordenar registros y limitar la cantidad de filas por página,

## ⚙️ Instalación y Uso

### 1. Clonar el repositorio
```bash
git clone https://github.com/Gengardeth/App-Web-Backend.git
cd App-Web-Backend
```

### 2. Crear un entorno virtual (recomendado)
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install django pillow
```

### 4. Aplicar migraciones
```bash
python manage.py migrate
```

### 5. Crear un superusuario para acceder al admin
```bash
python manage.py createsuperuser
```

### 6. Iniciar el servidor de desarrollo
```bash
python manage.py runserver
```

🧭 Rutas Principales

Sitio público:

Catálogo: http://localhost:8000/
Detalle producto: http://localhost:8000/producto/<id>/
Crear pedido: http://localhost:8000/pedir/<producto_id>/
Seguimiento: http://localhost:8000/seguimiento/<token>/`

## 📝 Notas de Desarrollo

- Migraciones: appTienda/migrations/
- Templates: appTienda/templates/appTienda/
- Static CSS: appTienda/static/css/styles.css
- Configuración del proyecto: PRUEBA_3_GONZALOLUIS/settings.py
- Archivos multimedia (imágenes): MEDIA_URL / MEDIA_ROOT (servidos en modo desarrollo)

## 👨‍💻 Autor

Gonzalo Rodriguez
Luis Carvajal

## 📄 Licencia

Este proyecto está bajo licencia MIT
