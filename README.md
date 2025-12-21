## 🚀 APIs REST y Reporte Dinámico (Evaluación Sumativa 4)

### Reporte Dinámico (Vista protegida)
- Ruta: `/reporte/` (requiere login)
- Permite filtrar por fecha y estado
- Muestra tabla de pedidos y gráfico de cantidad por estado (Chart.js)

### APIs REST (Django REST Framework)

#### API 1: CRUD de Insumos
- Ruta base: `/api/insumos/`
- Métodos permitidos: GET (lista y detalle), POST, PUT/PATCH, DELETE
- Ejemplo uso con curl:
```bash
curl -X GET http://localhost:8000/api/insumos/
curl -X POST -H "Content-Type: application/json" -d '{"nombre":"Tela roja","tipo":"Tela","cantDisponible":10}' http://localhost:8000/api/insumos/
```

#### API 2: Crear y modificar pedidos
- Ruta base: `/api/pedidos/`
- Métodos permitidos: POST (crear), PUT/PATCH (modificar)
- Métodos bloqueados: GET (colección), DELETE
- Ejemplo uso con curl:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"nombre_cliente":"Juan","contacto":"99999999","descripcion":"Pedido especial"}' http://localhost:8000/api/pedidos/
curl -X PUT -H "Content-Type: application/json" -d '{"estado_pedido":"aprobado"}' http://localhost:8000/api/pedidos/1/
```

#### API 3: Filtro de pedidos por parámetros
- Ruta: `/api/pedidos/filtrar/?fecha_inicio=2024-01-01&fecha_fin=2025-01-01&estados=aprobado&max_resultados=10`
- Permite filtrar por rango de fechas, estado(s) y cantidad máxima de resultados
- Ejemplo uso con curl:
```bash
curl -X GET "http://localhost:8000/api/pedidos/filtrar/?fecha_inicio=2024-01-01&fecha_fin=2025-01-01&estados=aprobado&max_resultados=10"
```

### Deploy y Producción
- El sistema está preparado para deploy en servicios como Render, Railway, PythonAnywhere, etc.
- Variables sensibles y de entorno gestionadas en `settings.py`
- Archivos estáticos y media configurados para producción

#### Usuario administrador para evaluación
Usuario: admin  |  Contraseña: admin

---
# App-Web-Backend

Aplicación web Django para gestionar una tienda personalizada con catálogo público, gestión de pedidos con token único, control de insumos y panel administrativo avanzado.

## 📋 Descripción

Sistema integral de gestión de tienda que permite:
- 📦 Registrar y rastrear pedidos con token único autogenerado
- 🏪 Gestionar productos con múltiples imágenes y categorías
- 📋 Control de insumos con información de inventario
- 🛍️ Catálogo público con búsqueda, filtros y productos destacados
- 🔍 Seguimiento público de pedidos sin autenticación
- 💾 Panel administrativo con filtros avanzados y búsqueda
- ✅ Validaciones en formularios y modelos de datos
- 🎨 Interfaz responsiva con Bootstrap 5.3.3

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
1. **Categorías**: Nombre y descripción para organizar productos
2. **Productos**: Nombre, descripción, precio base, hasta 3 imágenes, estado destacado
3. **Insumos**: Información de inventario con tipo, cantidad, marca y color
4. **Pedidos**: Registro completo con estados de pedido/pago, token de seguimiento y referencias

### Panel de Administración
- ✅ **Categorías**: Búsqueda y ordenamiento por nombre
- ✅ **Productos**: Filtros por categoría y destacado, búsqueda por nombre
- ✅ **Insumos**: Filtros por tipo, marca y color
- ✅ **Pedidos**: Filtros avanzados (plataforma, estado, pago, fecha), búsqueda por cliente/contacto/token
- ✅ Token de seguimiento solo lectura (autogenerado)
- ✅ Paginación y ordenamiento en todos los modelos

### Vistas Públicas
- ✅ **Catálogo**: Listado de productos con búsqueda y filtros
- ✅ **Detalle de Producto**: Visualización con imágenes y descripción
- ✅ **Crear Pedido**: Formulario para realizar solicitudes de personalización
- ✅ **Seguimiento**: Rastrear pedido por token sin autenticación

### Validaciones
- ✅ Contacto: Mínimo 6 caracteres, teléfono mínimo 8 dígitos
- ✅ Descripción de pedido: Mínimo 10 caracteres
- ✅ Fecha: No puede ser anterior a hoy
- ✅ Regla de negocio: Pedido no puede finalizarse si pago no está completado

## 🛠️ Requisitos

- Python 3.8+
- Django 5.2.8
- Pillow (para procesamiento de imágenes)
- pip (gestor de paquetes de Python)

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

### Público (sin autenticación):
- **Inicio/Catálogo**: `/` o `/catalogo/` - Listado de productos
- **Buscar Token**: `/buscar-token/?token=XXXX` - Redirecciona al seguimiento
- **Detalle Producto**: `/producto/<id>/` - Información detallada del producto
- **Crear Pedido**: `/pedido/<producto_id>/` - Formulario de solicitud personalizada
- **Seguimiento Pedido**: `/seguimiento/<token>/` - Rastrear estado del pedido

### Administración (autenticado):
- **Panel Admin**: `/admin/` - Gestión completa del sistema

## 📝 Notas de Desarrollo

- **Base de datos**: SQLite (`db.sqlite3`) - Cambiar a PostgreSQL/MySQL para producción
- **Archivos multimedia**: Guardados en `media/` con MEDIA_URL y MEDIA_ROOT configurados
- **Configuración**: `PRUEBA_3_GONZALOLUIS/settings.py` con idioma español y zona horaria Chile
- **Estilos CSS**: `appTienda/static/css/styles.css`
- **Migraciones**: `appTienda/migrations/` - Ejecutadas y funcionales
- **DEBUG**: Actualmente en `True` - **Cambiar a `False` en producción**

## 🔄 Flujo de la Aplicación

1. **Usuario visita catálogo**: Accede a la lista de productos con opción de buscar y filtrar
2. **Selecciona producto**: Ve detalles completos con imágenes
3. **Realiza pedido**: Completa formulario con datos personales y referencias
4. **Obtiene token**: Recibe token único para rastrear el pedido
5. **Rastrea pedido**: Puede ver el estado en cualquier momento usando el token
6. **Administrador gestiona**: Panel con filtros avanzados para gestionar pedidos

## 📊 Validaciones Implementadas

### Formulario de Pedido (PedidoForm)
- ✅ **Contacto**: Mínimo 6 caracteres, teléfono con mínimo 8 dígitos
- ✅ **Descripción**: Mínimo 10 caracteres, máximo 500 caracteres
- ✅ **Fecha**: No anterior a hoy, formato de fecha
- ✅ **Fotos**: Opcionales, aceptan JPEG/PNG
- ✅ **Estilos Bootstrap**: Widgets del formulario con clases de Bootstrap 5

### Modelo Pedido
- ✅ **Token único**: Autogenerado con UUID (10 caracteres)
- ✅ **Validación de coherencia**: Pedido finalizado solo si pago está completado
- ✅ **Estados controlados**: Mediante choices predefinidas
- ✅ **Fecha solicitada**: Opcional, sin validación retroactiva por defecto

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

5. **Funcionalidad agregada hoy (Frontend público)** 
✅Badge “Destacado” en Catálogo

Se incorporó un indicador visual en la vista pública del catálogo para identificar productos destacados.

Si un producto tiene es_destacado = True, se muestra una etiqueta “Destacado” en la tarjeta del producto.

Esto permite que el usuario vea claramente qué productos están marcados como destacados sin depender del panel de administración.

Archivo modificado:

appTienda/templates/appTienda/catalogo.html

✅ Cambios de interfaz aplicados hoy
Ajuste de Navbar (Base)

Se simplificó el menú superior para mantener solo los accesos principales del proyecto:

Enlace Tienda (vuelve al catálogo).

Botón Admin visible solo para usuarios is_staff.

Archivo modificado:

appTienda/templates/appTienda/base.html

✅ Evidencia / cómo probar

Ingresar al catálogo (/ o /catalogo).

Verificar que los productos con es_destacado muestran la etiqueta “Destacado” en su tarjeta.

Iniciar sesión como admin/staff y confirmar que aparece el botón Admin en la barra superior.
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
