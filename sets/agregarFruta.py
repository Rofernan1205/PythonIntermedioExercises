# Ejercicio
# Pide al usuario una fruta y  verifica en el conjunto y si existe no se debe agregar,
# del contrario agregar al conjunto


# Dado el conjunto:
frutas = {'manzana', 'pera', 'uva'}


def frutas_agregar(fruta):
    if fruta in frutas:
        print(f"Ya existe {fruta}")
    else:
        frutas.add(fruta)
        print(frutas)


frutas_agregar("pera")
