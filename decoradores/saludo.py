# Ejercicios
# Crea un decorador llamado logger que imprima "Llamando a la función" antes de ejecutarla y "Función finalizada"
# después.
# @logger
# def saludar():
#     print("Hola mundo")

def logger(my_funcion):
    def funcion(nombre):
        print("Hola buen dia")
        my_funcion(nombre)
        print("Nos vemos")
    return funcion


@logger
def saludar(nombre):
    print(f"{nombre}")


saludar("Rodrigo")
