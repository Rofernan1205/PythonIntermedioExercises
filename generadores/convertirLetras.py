# Ejercicio: Generador que reciba una lista y devuelva cada elemento en mayúsculas

def generador_mayusculas(lista):
    yield from lista


nombres = ["Rodrigo", "Fernando", "Sandro"]
for nombre in generador_mayusculas(nombres):
    print(nombre.upper())
