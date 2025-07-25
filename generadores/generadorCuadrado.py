# Generador de cuadrados
# Crea un generador que devuelva los cuadrados de los números del 1 al n.

def genere_cuadrados(limite):
    for numero in range(0, limite):
        yield numero ** 2


for cuadrado in genere_cuadrados(10):
    print(cuadrado)


