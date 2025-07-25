# Ejercicio: Queremos crear un decorador llamado loggear que:
# Reciba cualquier función.
# Antes de ejecutar esa función, muestre los argumentos que le mandamos.
# Luego ejecute la función original.
# Y finalmente muestre el resultado que devuelve.

# definir decorador
def loggear(funcion):
    def wrapper(*args, **kwargs):
        print(f"Llamando a {funcion.__name__}")
        print(f"Parametros son {args}, {kwargs}")
        resultado = funcion(*args, **kwargs)
        print(f"Resultado de la suma {resultado}")
        return resultado

    return wrapper


@loggear
def suma(a, b, c, d):
    return a + b + c + d


suma(1, 3, 5, d=12)
