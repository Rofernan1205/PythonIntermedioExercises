# Ejercicio
# Realizar un decorador que convierta una funcion de cadena de textoa en Mayusculas

def mayusculas(funcion):
    def wrapper(*args, **kwargs):
        cadena = funcion(*args, **kwargs)
        return cadena.upper()

    return wrapper


@mayusculas
def mi_nombre(nombre):
    return f"Yo soy {nombre}"


print(mi_nombre("Rodrigo"))
