# App-Web-Backend

Aplicación web Django para gestionar una tienda en línea con seguimiento de pedidos, gestión de insumos, administración de productos y catálogo público.

## 📋 Descripción

Sistema de gestión de tienda que permite:
- 📦 Registrar y dar seguimiento a pedidos con token único
- 🏪 Gestionar insumos y productos con múltiples imágenes
- 👥 Administrar datos de clientes y contactos
- 🛍️ Catálogo público de productos con búsqueda avanzada y filtros
- 🔍 Rastrear pedidos mediante token único y URL compartible
- 💾 Panel de administración optimizado con filtros y búsqueda
- ✅ Validación de datos en formularios y modelos
- 🎨 Interfaz responsiva con Bootstrap 5

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

## 🧭 Rutas Principales

### Sitio Público:
- **Catálogo**: `http://localhost:8000/`
- **Detalle de Producto**: `http://localhost:8000/producto/<id>/`
- **Crear Pedido**: `http://localhost:8000/pedir/<producto_id>/`
- **Rastrear Pedido**: `http://localhost:8000/seguimiento/<token>/`

### Panel de Administración:
- **Admin Panel**: `http://localhost:8000/admin/`

## 📝 Notas de Desarrollo

- **Migraciones**: `appTienda/migrations/`
- **Templates**: `appTienda/templates/appTienda/`
- **Estilos CSS**: `appTienda/static/css/styles.css`
- **Configuración del proyecto**: `PRUEBA_3_GONZALOLUIS/settings.py`
- **Archivos multimedia**: Servidos en modo desarrollo (imágenes de productos y pedidos)
- **Base de datos**: SQLite (db.sqlite3) - cambiar para producción

## 🔄 Flujo de la Aplicación

1. **Usuario visita catálogo**: Accede a la lista de productos con opción de buscar y filtrar
2. **Selecciona producto**: Ve detalles completos con imágenes
3. **Realiza pedido**: Completa formulario con datos personales y referencias
4. **Obtiene token**: Recibe token único para rastrear el pedido
5. **Rastrea pedido**: Puede ver el estado en cualquier momento usando el token
6. **Administrador gestiona**: Panel con filtros avanzados para gestionar pedidos

## 📊 Validaciones Implementadas

### Formulario de Pedido (PedidoForm)
- ✅ Validación de contacto (teléfono o email)
- ✅ Descripción mínima de 10 caracteres
- ✅ Campos de foto opcionales
- ✅ Fecha de pedido configurable
- ✅ Widgets Bootstrap para mejor UX

### Modelo Pedido
- ✅ Token de seguimiento único y automático
- ✅ Validación: Pedido no puede ser "Finalizado" si pago no está "Pagado"
- ✅ Estados de pedido controlados por choices
- ✅ Estados de pago validados

## 👨‍💻 Autores

- Gonzalo Rodriguez
- Luis Carvajal

## 📄 Licencia

Este proyecto está bajo licencia MIT

## 👨‍💻 Autor

Gonzalo Rodriguez
Luis Carvajal

## 📄 Licencia

Este proyecto está bajo licencia MIT
