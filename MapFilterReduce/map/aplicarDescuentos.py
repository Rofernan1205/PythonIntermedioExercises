# Ejercicio: Tienes una lista de diccionarios con información de productos. Usa map() para extraer solo los precios
# con descuento (10% menos).


productos = [
    {'nombre': 'camisa', 'precio': 100},
    {'nombre': 'pantalón', 'precio': 150},
    {'nombre': 'zapatos', 'precio': 200}
]


def aplicar_descuento(porcentaje, lista):
    descuento = porcentaje / 100
    product_des = list(map(lambda x: {
        "nombre": x["nombre"],
        "precio": x["precio"] - x["precio"] * descuento
    }, lista))
    return product_des


salida = aplicar_descuento(10, productos)
print(salida)
