class Carrito: 
    def __init__(self, request): 
        self.request = request 
        self.session = request.session 
        carrito = self.session.get("carrito")
        if not carrito: 
            carrito = self.session["carrito"] = {}
        self.carrito = carrito 
    
    def agregar(self,variante): 
        if str(variante.id) not in self.carrito: 
            self.carrito[str(variante.id)] = {
                "variante_id": variante.id,
                "nombre": variante.perfume.nombre,
                "marca": variante.perfume.marca.nombre,
                "mililitros": variante.mililitros,
                "precio": float(variante.precio),
                "cantidad": 1,
                "imagen": variante.perfume.imagen.url if variante.perfume.imagen else "",
                "total": float(variante.precio)
            }
        else:
            # Si ya existe, sumamos uno a la cantidad
            self.carrito[str(variante.id)]["cantidad"] += 1
            self.carrito[str(variante.id)]["total"] += float(variante.precio)
        self.guardar()


    def guardar(self):
        self.session.modified = True

    def eliminar(self, variante):
        variante_id = str(variante.id)
        if variante_id in self.carrito:
            del self.carrito[variante_id]
            self.guardar()

    def restar(self, variante):
        variante_id = str(variante.id)
        if variante_id in self.carrito:
            self.carrito[variante_id]["cantidad"] -= 1
            self.carrito[variante_id]["total"] -= float(variante.precio)
            if self.carrito[variante_id]["cantidad"] < 1:
                self.eliminar(variante)
            self.guardar()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True