from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Importamos TODAS las vistas nuevas
from tienda.views import inicio, detalle, agregar_producto, eliminar_producto, restar_producto, limpiar_carrito, ver_carrito, procesar_pedido

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('perfume/<int:perfume_id>/', detalle, name='detalle'),
    
    # --- RUTAS DEL CARRITO ---
    path('agregar/<int:variante_id>/', agregar_producto, name='agregar'),
    path('eliminar/<int:variante_id>/', eliminar_producto, name='eliminar'),
    path('restar/<int:variante_id>/', restar_producto, name='restar'),
    path('limpiar/', limpiar_carrito, name='limpiar'),
    path('carrito/', ver_carrito, name='ver_carrito'),
    path('checkout/', procesar_pedido, name='procesar_pedido'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)