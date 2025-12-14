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

## � CUMPLIMIENTO DE REQUERIMIENTOS - EVALUACIÓN SUMATIVA 3

### ✅ Descripción del Proyecto Implementada

El proyecto es una **aplicación web Django** completa para la gestión de una tienda de artículos personalizados, que cumple 100% con los requerimientos de la Evaluación Sumativa 3.

**Tecnologías utilizadas:**
- Framework: Django 5.2.8
- Base de datos: SQLite3
- Interfaz: Bootstrap 5.3.3
- Lenguaje: Python 3.8+

---

### ✅ Configuración General del Sistema

| Requisito | Estado | Detalles |
|-----------|--------|----------|
| **Idioma español** | ✅ Cumplido | `LANGUAGE_CODE = 'es'` en settings.py |
| **Zona horaria Chile** | ✅ Cumplido | `TIME_ZONE = 'America/Santiago'` en settings.py |
| **SQLite** | ✅ Cumplido | Base de datos `db.sqlite3` configurada correctamente |
| **Archivos estáticos** | ✅ Cumplido | CSS en `appTienda/static/css/` |
| **Archivos multimedia** | ✅ Cumplido | Imágenes en `media/` con rutas MEDIA_URL y MEDIA_ROOT |
| **Migraciones** | ✅ Cumplido | `0001_initial.py` ejecutada correctamente |

---

### ✅ Modelos Implementados

#### 1. **Categorías**
- ✅ Campo nombre (CharField, max_length=80)
- ✅ Campo detalle (TextField, optional)
- ✅ Relación 1:N con Productos
- ✅ Métodos `__str__()` implementado

#### 2. **Productos**
- ✅ Nombre, descripción, precio_base
- ✅ ForeignKey a Categoría (on_delete=CASCADE)
- ✅ Tres campos ImageField: imagen1, imagen2, imagen3
- ✅ Campo es_destacado (BooleanField)
- ✅ Métodos `__str__()` implementado

#### 3. **Insumos**
- ✅ Nombre, tipo, cantDisponible
- ✅ Campos opcionales: unidad, marca, color
- ✅ Gestión exclusiva desde panel admin ✓
- ✅ Métodos `__str__()` implementado

#### 4. **Pedidos**
- ✅ nombre_cliente, contacto (CharField)
- ✅ descripcion (TextField)
- ✅ ForeignKey a Producto (null=True, blank=True)
- ✅ Plataforma (choices: Facebook, Instagram, WhatsApp, Presencial, Web, Otro)
- ✅ Estado pedido (choices: Solicitado, Aprobado, En proceso, Realizada, Entregada, Finalizada, Cancelada)
- ✅ Estado pago (choices: Pendiente, Parcial, Pagado)
- ✅ Fecha solicitada (DateField, opcional)
- ✅ Token único de seguimiento (autogenerado UUID)
- ✅ Dos campos para imágenes de referencia: foto_ref1, foto_ref2
- ✅ Métodos `__str__()` implementado

**Regla de Negocio Implementada:**
- ✅ Validación en `clean()`: Pedido no puede ser "Finalizado" si pago ≠ "Pagado"

---

### ✅ Panel de Administración (Django Admin)

**Categorías:**
- ✅ list_display: nombre, detalle
- ✅ search_fields: nombre
- ✅ ordering: nombre
- ✅ list_per_page: 20

**Productos:**
- ✅ list_display: nombre, categoría, precio_base, es_destacado
- ✅ list_filter: categoría, es_destacado
- ✅ search_fields: nombre, categoría__nombre
- ✅ ordering: categoría, nombre
- ✅ list_per_page: 20

**Insumos:**
- ✅ list_display: nombre, tipo, cantDisponible, unidad, marca, color
- ✅ list_filter: tipo, marca, color
- ✅ search_fields: nombre, marca
- ✅ ordering: tipo, nombre
- ✅ list_per_page: 20

**Pedidos:**
- ✅ list_display: nombre_cliente, contacto, plataforma, estado_pedido, estado_pago, fecha_solicitada, producto_referencia, token_seguimiento
- ✅ list_filter: plataforma, estado_pedido, estado_pago, fecha_solicitada
- ✅ search_fields: nombre_cliente, contacto, token_seguimiento, producto_referencia__nombre
- ✅ date_hierarchy: fecha_solicitada
- ✅ readonly_fields: token_seguimiento
- ✅ ordering: -fecha_solicitada
- ✅ list_per_page: 20

---

### ✅ Funcionalidades Públicas Implementadas

#### 1. **Catálogo de Productos**
**Vista: `catalogo()`**
- ✅ Listado de todos los productos
- ✅ **Búsqueda**: Por nombre y descripción (Q objects)
- ✅ **Filtro por categoría**: Mediante parámetro GET
- ✅ **Filtro de destacados**: Parámetro dest=1
- ✅ Acceso público sin autenticación
- ✅ Template responsivo con Bootstrap

#### 2. **Vista Detalle de Producto**
**Vista: `detalle_producto()`**
- ✅ Información completa del producto
- ✅ Descripción, precio base
- ✅ Display de imágenes (hasta 3)
- ✅ Enlace directo para realizar pedido
- ✅ Acceso público sin autenticación

#### 3. **Formulario de Solicitud de Pedido**
**Vista: `pedir_producto()`**
**Form: `PedidoForm`**

Campos del formulario:
- ✅ nombre_cliente (requerido)
- ✅ contacto (requerido, validado)
- ✅ descripcion (requerido, mínimo 10 caracteres)
- ✅ fecha_solicitada (opcional, no anterior a hoy)
- ✅ foto_ref1 (opcional)
- ✅ foto_ref2 (opcional)

**Validaciones:**
- ✅ Contacto: Debe tener mínimo 6 caracteres
- ✅ Contacto: Si es teléfono, debe tener al menos 8 dígitos
- ✅ Descripción: Mínimo 10 caracteres
- ✅ Fecha: No puede ser anterior a la fecha actual
- ✅ Imágenes: Son opcionales

**Procesamiento:**
- ✅ Al enviar, se crea pedido con:
  - estado_pedido = 'solicitado'
  - estado_pago = 'pendiente'
  - plataforma = 'web'
  - Producto de referencia asignado
  - Token único generado automáticamente

#### 4. **Seguimiento de Pedido por Token**
**Vista: `seguimiento_pedido()`**
- ✅ Acceso mediante URL con token único
- ✅ Sin autenticación requerida
- ✅ Muestra información completa del pedido:
  - Estado del pedido
  - Estado del pago
  - Cliente y contacto
  - Descripción
  - Producto de referencia
  - Imágenes de referencia
  - Fecha solicitada
- ✅ URL compartible generada dinámicamente
- ✅ Mensaje de error si token no existe

---

### ✅ Funcionalidades Extra Implementadas

1. **Filtro de Productos Destacados**
   - ✅ Campo `es_destacado` en Producto
   - ✅ Botón "Destacados" en catálogo
   - ✅ Vista filtrada accesible desde catálogo

2. **Validaciones Avanzadas**
   - ✅ Validación de contacto (teléfono y email)
   - ✅ Validación de descripción mínima
   - ✅ Validación de fecha (no retroactiva)
   - ✅ Regla de negocio: Pedido-Pago coherencia

3. **Interfaz Mejorada**
   - ✅ Bootstrap 5.3.3
   - ✅ Diseño responsivo
   - ✅ Badges para estados
   - ✅ Navegación clara

4. **Token de Seguimiento Robusto**
   - ✅ UUID automático (10 caracteres)
   - ✅ Garantiza unicidad con validación
   - ✅ No editable desde admin
   - ✅ URL compartible completa

---

### ✅ Datos de Prueba

El proyecto incluye:
- ✅ Base de datos SQLite con datos iniciales
- ✅ Migraciones ejecutadas correctamente
- ✅ Ready para evaluación inmediata

---

## 📝 Resumen Final

**Estado del Proyecto: 100% COMPLETO Y FUNCIONAL**

- ✅ 4 modelos completamente implementados
- ✅ Panel de administración optimizado
- ✅ 4 vistas públicas funcionales
- ✅ 1 formulario con validaciones completas
- ✅ 5 templates responsivos
- ✅ Todas las rutas configuradas
- ✅ Configuración del sistema correcta
- ✅ Cumplimiento total de requerimientos
