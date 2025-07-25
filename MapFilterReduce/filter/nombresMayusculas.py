# Enunciado
# Dada una lista de nombres con diferentes longitudes, filtra los nombres que tienen más de 5 letras y convierte los
# que pasaron el filtro a mayúsculas.
# nombres = ["Ana", "Mariana", "Luis", "Fernando", "Eva", "Beatriz"]

nombres = ["Ana", "Mariana", "Luis", "Fernando", "Eva", "Beatriz"]


def filter_map(numero, lista):
    nueva_lista = list(filter(lambda x: len(x) >= numero, lista))
    lista_mayus = list(map(lambda x: x.upper(), nueva_lista))
    return lista_mayus


resultado = filter_map(8, nombres)
print(resultado)
