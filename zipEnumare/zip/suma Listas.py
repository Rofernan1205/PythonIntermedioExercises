# Objetivo: Crear una lista suma = [5, 7, 9] usando zip
# de las isguientes listas
# a = [1, 2, 3]
# b = [4, 5, 6]

a = [1, 2, 3]
b = [4, 5, 6]

def suma_listas(lista1,lista2):
    lista_res = [x+y for x, y in zip(a,b)]
    return lista_res

lista_suma = suma_listas(a, b)
print(lista_suma)
