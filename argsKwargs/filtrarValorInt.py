# Ejercicio: Filtrar solo los valores tipo int de *args
# Crea una función que reciba cualquier cantidad de argumentos, y devuelva solo los números enteros en una lista.

def filtrar_tipo_dato(*args):
    enteros = [dato for dato in args if isinstance(dato, int)]
    print(enteros)


filtrar_tipo_dato(1, 3, "prueba", "12", 2)
