# Ejercici
# Verificar cuantos elementos unicos hay y cuales son
nombres = ['sol', 'luna', 'sol', 'estrella']


def palabras_unicos(lista):
    lista_set = set(lista)
    print(f"Cantidad de nombres : {len(lista_set)}")
    print("Nombres")
    for nombre in lista_set:
        print(nombre)


palabras_unicos(nombres)
