# Ejercicio
# Leer el archivo json de usuarios, ingresar un usuario y contraseña desde la consola
# Si el usuario está logueado (logueado = True), muestra "Bienvenido", si no "Por favor inicia sesión".

import json


def leer_archivo(file):
    try:
        with open(file, "r") as f:
            usuarios = json.load(f)
            return usuarios
    except ValueError as err:
        raise ValueError(err)


def login(user, passw, file):
    datos = leer_archivo(file)
    for dato in datos:
        log_user = True if dato["usuario"] == user and dato["password"] == passw else False
        if log_user:
            return True
    return False


var = True
while var:
    usuario = input("Usuario : ").strip()
    password = input("Password : ").strip()
    data = login(usuario, password, "usuarios.json")
    if data:
        var = False
    else:
        print("No existe usuario")
