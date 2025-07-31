# Ejercicio
# Realizar un decorador que permite repetir n vecez @repetir(n)

def repetir(n):
    def my_funcion(funcion):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                funcion(*args, **kwargs)
        return wrapper
    return my_funcion


@repetir(3)
def saludo(nombre):
    print(f"Buenos dias {nombre}")


saludo("Rodrigo")