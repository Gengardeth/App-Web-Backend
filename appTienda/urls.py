from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo, name='catalogo'),
    path('buscar-token/', views.buscar_token, name='buscar_token'),
    path('producto/<int:id>/', views.detalle_producto, name='detalle_producto'),
    path('pedido/<int:producto_id>/', views.pedir_producto, name='pedir_producto'),
    path('seguimiento/<str:token>/', views.seguimiento_pedido, name='seguimiento_pedido'),
]
