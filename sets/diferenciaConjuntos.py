# Ejercicios
# Dado dos listas
# A = {1, 2, 3, 4}
# B = {3, 4, 5}
# Mostrar elementos que está en el conjunto A pero no en el B
A = {1, 2, 3, 4}
B = {3, 4, 5}


def diferencia_conjunto(con1, con2):
    nuevo_conj = con1 - con2
    return nuevo_conj


resultado = diferencia_conjunto(A, B)
print(resultado)


