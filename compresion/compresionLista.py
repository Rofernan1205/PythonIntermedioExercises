# Generar una lista sin usar compresión
def sin_compresion(num):
    lista = []
    for numero in range(num):
        lista.append(numero ** 2)
    return lista


print(sin_compresion(4))


# Ahora usando compresión

def con_compresion(num):
    lista = [numero ** 2 for numero in range(num)]
    return lista


print(con_compresion(4))

# También se puede usar con filtro

def con_compresion_filtro():
    nombres = ["Luis", "Ana", "Anabel", "Kiara"]
    nombres_a = [nombre for nombre in nombres if nombre[0] == "A"]
    return nombres_a

print(con_compresion_filtro())
