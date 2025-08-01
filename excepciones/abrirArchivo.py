# Ejercicio
# Abrir un archivo y capturar error si en caso que no exista

try:
    with open("archivo.txt", "r") as f:
        contenido = f.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no existe.")
