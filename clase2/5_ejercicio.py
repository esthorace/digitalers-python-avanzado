"""
✨ EJERCICIO ✨

A partir del siguiente diccionario, realizar los ejercicios propuestos:

inventario = {
    "manzanas": 10,
    "naranjas": 5,
    "peras": 8
}

1. Se compraron 5 manzanas.
2. Se vendieron 3 naranjas.
3. Se compraron 5 uvas.
4. Solicitar al usuario qué producto está buscando, y, si está disponible,
pedir la cantidad, venderlo y mostrar el inventario. La cantidad no debe superar el stock.
5. Crear un nuevo diccionario con 3 productos, agregarlos al diccionario principal.
6. Calcular el número total de productos del inventario.
"""

inventario = {"manzanas": 10, "naranjas": 5, "peras": 8}
inventario["manzanas"] += 5
inventario["naranjas"] -= 3
inventario["uvas"] = 5

producto = input("¿Qué producto está buscando? ").lower().strip()
if producto in inventario:
    cantidad = int(input("¿Cuántas unidades desea comprar? "))
    if cantidad <= inventario.get(producto, 0):
        inventario[producto] -= cantidad
        print(f"✅ Venta realizada. Quedan {inventario[producto]} {producto}")
    else:
        print(f"No hay tanta cantidad. Solo quedan {inventario[producto]}")
else:
    print(f"El producto {producto} no está disponible")

nuevos_productos = {
    "kiwis": 10,
    "mangos": 5,
    "sandias": 8,
}
# inventario = {**inventario, **nuevos_productos}
inventario.update(nuevos_productos)
print(inventario)

total_productos = sum(inventario.values())
print(f"El número total de productos es: {total_productos}")
