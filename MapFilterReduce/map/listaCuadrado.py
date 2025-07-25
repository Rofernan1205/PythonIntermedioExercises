# Ejercicio, dada una lista de nuemor elevar al cudrado cada uno de ellos.
# Usar map

def genera_lista(limite):
    numeros = [num for num in range(1, limite)]
    return numeros


def cuadrado_numeros(lista):
    cuadrado_list = map(lambda n: n ** 2, lista)
    return list(cuadrado_list)


lista_num = genera_lista(10)
cuadrados = cuadrado_numeros(lista_num)
print(cuadrados)

