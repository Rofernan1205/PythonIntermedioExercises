# Dado la lista

nombres = ["Ana", "Luis", "Marta", "Pedro", "Lucía"]

# Objetivo: Imprimir solo los elementos con índice par.

def indice_pares(lista):
    for indice, valor in enumerate(lista):
        if indice % 2 == 0 :
            print(valor)



indice_pares(nombres)