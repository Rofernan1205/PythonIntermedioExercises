# Ejercicio Crear usuario con valores por defecto Crea una función crear_usuario que reciba **kwargs y devuelva un
# diccionario con nombre, edad y país. Si no se pasan esos datos, usa valores por defecto.

def crear_usurio(**kwargs):
    nombre = kwargs.get("nombre", "Sin nombre")
    edad = kwargs.get("edad", 0)
    pais = kwargs.get("pais", "Sin nacionalidad")
    usuario = {"nombre": nombre, "edad": edad, "pais": pais}
    print(usuario)


crear_usurio(pais="Peru")
