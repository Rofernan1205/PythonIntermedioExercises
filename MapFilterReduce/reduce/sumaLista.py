# Ejercicio
# Sumar los valores de una lista usando reducer
# importar libreria
from functools import reduce

numeros = [1, 12, 14, 10, 2, 22]


def sumar_valores_lista(lista):
    return reduce(lambda x, y: x + y, lista)


resultado = sumar_valores_lista(numeros)
print(resultado)
