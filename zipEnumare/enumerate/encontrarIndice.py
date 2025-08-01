# Dado la lista
# valores = [10, 20, 30, 40]
# Objetivo: Imprimir el índice donde está el valor 30.

valores = [10, 20, 30, 40]
def buscar_valor_indice(lista, valor):
    for indice, numero in enumerate(lista):
        if numero == valor:
            print(f"El {numero} esta en el indice {indice}")


buscar_valor_indice(valores, 30)