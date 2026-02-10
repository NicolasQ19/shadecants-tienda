from django.shortcuts import render, get_object_or_404, redirect
from .models import Perfume, Variante 
from .carrito import Carrito 
import urllib.parse


def inicio(request):
    # Buscamos todos los perfumes en la base de datos
    perfumes = Perfume.objects.all()
    # Se los enviamos al HTML
    return render(request, 'tienda/inicio.html', {'perfumes': perfumes})


def detalle(request, perfume_id):
    perfume = get_object_or_404(Perfume, id=perfume_id)

    return render(request, 'tienda/detalle.html', {'perfume': perfume})

# --- FUNCIONES DEL CARRITO ---

def agregar_producto(request, variante_id):
    carrito = Carrito(request)
    variante = get_object_or_404(Variante, id=variante_id)
    carrito.agregar(variante=variante)
    # Redirigimos a la página del carrito para que vea lo que agregó
    return redirect('ver_carrito')

def eliminar_producto(request, variante_id):
    carrito = Carrito(request)
    variante = get_object_or_404(Variante, id=variante_id)
    carrito.eliminar(variante=variante)
    return redirect('ver_carrito')

def restar_producto(request, variante_id):
    carrito = Carrito(request)
    variante = get_object_or_404(Variante, id=variante_id)
    carrito.restar(variante=variante)
    return redirect('ver_carrito')

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('ver_carrito')

def ver_carrito(request):
    return render(request, 'tienda/carrito.html')


def procesar_pedido(request):
    carrito = request.session.get('carrito', {})
    if not carrito:
        return redirect('inicio')
    
    # Armamos el mensaje
    texto = "Hola Shadecants! 👋 Quiero realizar el siguiente pedido:\n\n"
    total = 0
    
    for key, item in carrito.items():
        subtotal = item['precio'] * item['cantidad']
        texto += f"🔹 {item['cantidad']}x {item['nombre']} ({item['mililitros']}ml) - ${subtotal}\n"
        total += subtotal
    
    texto += f"\n💰 *TOTAL A PAGAR: ${total}*"
    texto += "\n\nQuedo a la espera de los datos para transferir."
    
    # Codificamos el mensaje para internet
    mensaje_url = urllib.parse.quote(texto)
    
    # TU NÚMERO DE WHATSAPP AQUÍ (Formato internacional sin +)
    # Ejemplo: 54911 y tu numero. Reemplázalo abajo:
    mi_numero = "541166129771" 
    
    url_whatsapp = f"https://wa.me/{mi_numero}?text={mensaje_url}"
    
    # Opcional: Limpiar el carrito después de pedir
    request.session["carrito"] = {} 
    
    return redirect(url_whatsapp)