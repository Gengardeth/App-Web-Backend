# Informe Técnico: Reporte del Sistema

**Evaluación:** TI2041_ES4_Tienda_API_Deploy_v3

## 1. Introducción
Este informe documenta la implementación y evidencia funcional del "Reporte del sistema" solicitado en la evaluación. El reporte es una vista protegida que presenta métricas reales desde la base de datos, permite filtros personalizables y muestra los resultados en una tabla y un gráfico.

## 2. Criterios Evaluados
- Reporte del sistema
- Deploy
- APIs REST (DRF)
- Evaluación individual

## 3. Requerimiento: Reporte del Sistema 

### 3.1. Métricas reales desde la base de datos
El reporte utiliza consultas ORM para obtener datos reales de pedidos y productos, sin datos simulados ni hardcodeados.

### 3.2. Vista protegida
La ruta `/reporte/` requiere autenticación de usuario para acceder, garantizando la protección de la información.

### 3.3. Filtros personalizables
El usuario puede filtrar los resultados por:
- Rango de fechas
- Estado del pedido
- Plataforma de origen

### 3.4. Presentación en tabla
Se muestra una tabla con los pedidos filtrados, incluyendo columnas de ID, cliente, estado, fecha y plataforma.

### 3.5. Gráfico
Se incluye un gráfico de barras (Chart.js) que visualiza la cantidad de pedidos por estado.

## 4. Evidencia Funcional

### 4.1. Captura de la tabla de pedidos
![Captura de tabla de pedidos](Pega_aquí_tu_captura_tabla.png)

### 4.2. Captura del gráfico de pedidos por estado
![Captura de gráfico de pedidos](Pega_aquí_tu_captura_grafico.png)

### 4.3. Filtros aplicados
Ejemplo: Fecha inicio: 2025-01-01, Fecha fin: 2025-12-31, Estado: aprobado

## 5. Conclusión
El reporte cumple con todos los requisitos: utiliza datos reales, es accesible solo para usuarios autenticados, permite personalización mediante filtros y presenta la información de forma clara y visual.

---

_Este informe sirve como evidencia documentada y explicable del cumplimiento del requerimiento de reporte del sistema._
