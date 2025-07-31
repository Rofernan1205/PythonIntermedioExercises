# Ejercicio
# Realizar una función contador que almacene resultado en una variable global

# numero = 0
#
#
# def contador():
#     global numero
#     numero += 1
#
#
# contador()
# print(numero)
# contador()
# print(numero)
# contador()
# print(numero)

# Sin usar global/ buenas prácticas


numero = 0


def contador(num):
    return num + 1


salida = contador(numero)

print(salida)
