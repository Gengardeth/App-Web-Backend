# App-Web-Backend

Aplicación web Django para gestionar una tienda en línea con seguimiento de pedidos, gestión de insumos y administración de clientes.

## 📋 Descripción

Sistema de gestión de tienda que permite:
- 📦 Registrar y dar seguimiento a pedidos
- 🏪 Gestionar insumos y productos
- 👥 Administrar datos de clientes
- 🔍 Rastrear pedidos con token único
- 💾 Interfaz de administración completa

## 📁 Estructura del Proyecto

```
PRUEBA_3_GONZALOLUIS/
├── manage.py                      # Script de gestión de Django
├── README.md                      # Este archivo
├── PRUEBA_3_GONZALOLUIS/          # Configuración del proyecto
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── appTienda/                     # Aplicación principal
│   ├── migrations/                # Migraciones de base de datos
│   ├── templates/
│   │   └── appTienda/
│   │       └── base.html          # Template base
│   │       └── seguimiento_pedido.html
│   ├── __init__.py
│   ├── admin.py                   # Configuración de administrador
│   ├── apps.py
│   ├── models.py                  # Modelos de datos
│   ├── tests.py
│   └── views.py                   # Vistas de la aplicación
└── .gitignore
```

## ✨ Características Implementadas

### Modelos de Datos
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
- ✅ Página de seguimiento de pedidos

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

El servidor estará disponible en `http://localhost:8000`
Panel de administración: `http://localhost:8000/admin`

## 📝 Notas de Desarrollo

- Las migraciones se encuentran en `appTienda/migrations/`
- Los templates se organizan en `appTienda/templates/appTienda/`
- La configuración del proyecto está en `PRUEBA_3_GONZALOLUIS/settings.py`

## 👨‍💻 Autor

Gonzalo Luis

## 📄 Licencia

Este proyecto está bajo licencia MIT