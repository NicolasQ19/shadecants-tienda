def importe_total_carrito(request):
    total = 0
    cantidad_items = 0
    if request.user.is_authenticated or not request.user.is_authenticated:
        if "carrito" in request.session:
            for key, value in request.session["carrito"].items():
                total += float(value["precio"]) * int(value["cantidad"])
                cantidad_items += int(value["cantidad"])
    
    return {"importe_total_carrito": total, "cantidad_items_carrito": cantidad_items}