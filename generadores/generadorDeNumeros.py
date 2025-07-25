# Enunciado:
# Crea una función generadora que reciba un número n y produzca los números desde 0 hasta n.

def generador_numeros(limite):
    for numero in range(0, limite):
        yield numero


for n in generador_numeros(10):
    print(n)


# Enunciado:
# Crea un generador que reciba un número n y produzca todos los números pares desde 0 hasta n.

def generador_numeros_pares(limite):
    for numero in range(1, limite):
        if numero % 2 == 0:
            yield numero


for num in generador_numeros_pares(10):
    print(num)
