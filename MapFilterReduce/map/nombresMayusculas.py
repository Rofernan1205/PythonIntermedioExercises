# Ejercicios
# Convertir una lista de nombre en mayuscula usando map

nombres = ["Rodrigo", "Fernando", "Sandro"]


def nombres_mayusculaas(lista):
    nombres_mayus = list(map(lambda n: n.upper(), lista))
    return nombres_mayus


print(nombres_mayusculaas(nombres))
