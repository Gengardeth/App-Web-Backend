from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'insumos', views.InsumoViewSet, basename='insumo')
router.register(r'pedidos', views.PedidoViewSet, basename='pedido')

urlpatterns = [
    path('', views.catalogo, name='catalogo'),
    path('buscar-token/', views.buscar_token, name='buscar_token'),
    path('producto/<int:id>/', views.detalle_producto, name='detalle_producto'),
    path('pedido/<int:producto_id>/', views.pedir_producto, name='pedir_producto'),
    path('seguimiento/<str:token>/', views.seguimiento_pedido, name='seguimiento_pedido'),
    path('reporte/', views.reporte, name='reporte'),
    path('api/pedidos/filtrar/', views.PedidoFiltrarAPIView.as_view(), name='api-pedidos-filtrar'),
    path('api/', include(router.urls)),
]
