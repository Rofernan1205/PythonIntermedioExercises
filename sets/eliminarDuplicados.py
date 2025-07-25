# Elimina los ducplicados de una lista y guardar en una lista nueva usando sets

numeros = [1, 2, 2, 3, 4, 4, 5]


def eliminar_duplicados(lista):
    lista_set = set(lista)
    return lista_set


resultado = eliminar_duplicados(numeros)
print(resultado)

