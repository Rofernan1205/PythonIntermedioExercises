# Ejercicio
# Genere una lista de números, luego filtra los pares y los impares en dos
# listas diferentes usar filter

def generador_numeros(limite):
    return [num for num in range(1, limite)]


def coleccionar_pares(lista):
    lista_pares = list(filter(lambda n: n % 2 == 0, lista))
    lista_impares = list(filter(lambda n: n % 2 != 0, lista))
    return lista_pares, lista_impares


try:
    numero = int(input("Ingrese numero: "))
    resultado = generador_numeros(numero)
    pares, impares = coleccionar_pares(resultado)
    print(f"Pares {pares}")
    print(f"Impares {impares}")

except TypeError as err:
    raise TypeError(err)
