# Dada una lista de números y un número objetivo, imprime "Encontrado"
# si el número está en la lista, o "No encontrado" si no está. Usa for-else.

numeros = [10, 22, 35, 47, 53, 68]
objetivo = 32



def buscar_item(lista, item):
    for indice, numero in enumerate(numeros):
        if item == numero:
            print(f"El valor {numero} se encuentra en en indice {indice}")
            break
    else:
        print(f"No se encontro en la lista")


buscar_item(numeros, objetivo)
