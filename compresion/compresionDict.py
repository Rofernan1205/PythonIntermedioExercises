# Compresión de dict
# Crea un diccionario de cudradros de numeros
# Sin compresión
numeros = [item for item in range(5)]

def cuadrados(lista):
    dict_num = dict()
    for item in lista:
        dict_num[item] = item **2
    return dict_num

print(cuadrados(numeros))

# Con compresión

def dict_cuadrados(lista):
    dict_num = {dato : dato **2 for dato in lista if dato%2 ==0 }
    return dict_num
print(dict_cuadrados(numeros))

