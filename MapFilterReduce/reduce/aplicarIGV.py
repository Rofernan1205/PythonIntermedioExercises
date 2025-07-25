# Enunciado:
# Dado un listado de precios con impuestos incluidos, extrae el precio sin impuestos (asume 18%)
# y calcula el total de todos los precios netos.
from functools import reduce

precios_bruto = [118, 236, 59, 177]


def map_reduce(lista):
    precios_neto = list(map(lambda x: x - x * 0.18, lista))
    print(precios_neto)
    subtotal = reduce(lambda a, b: a + b, precios_neto)
    return subtotal


resultado = map_reduce(precios_bruto)
print(resultado)