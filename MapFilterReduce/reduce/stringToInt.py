# Enunciado:
# Dada una lista de strings que representan números, filtra los que son múltiplos de 3,
# convierte cada uno en entero y calcula la suma total.
from functools import reduce

datos = ["10", "15", "21", "30", "8", "9"]


def map_filter_reducer(lista):
    lista_int = list(map(lambda x: int(x), lista))
    multi_tres = list(filter(lambda x: x % 3 == 0, lista_int))
    total = reduce(lambda x, y: x + y, multi_tres)
    return total


resultado = map_filter_reducer(datos)
print(resultado)
