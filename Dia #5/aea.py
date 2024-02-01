Tabla = {
    "Productos": ("Manzana", "Computador", "Hacienda", "Celular"),
    "Precios": (2500, 200, 250000000, 300000)
}

print("PRODUCTOS \tPRECIOS")
for i in range(4):
    print(Tabla["Productos"][i], "\t", Tabla["Precios"][i])

Producto = str(input("Digite el producto que desea: "))
Producto = Producto.capitalize()

if Producto in Tabla["Productos"]:
    Cantidad = int(input(f"Digite la cantidad de {Producto.lower()}s que desea: "))
    indice_producto = Tabla["Productos"].index(Producto)
    PrecioTotal = Tabla["Precios"][indice_producto] * Cantidad
    print(f"El precio total de {Cantidad} {Producto.lower()}s es: {PrecioTotal}")
else:
    print(f"Lo siento, el producto {Producto} no está en la tabla.")
