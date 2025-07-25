# Ejercicio
# Filtrar nombres por letra de una lista usando filter

personas = [
    {id: 1, "nombre": "Rodrigo", "correo": "rodrigo@hotmail.com", "edad": 28},
    {id: 2, "nombre": "Fernando", "correo": "fernando@hotmail.com", "edad": 23},
    {id: 3, "nombre": "Sandro", "correo": "sandro@hotmail.com", "edad": 19},
    {id: 4, "nombre": "Liz", "correo": "liz@hotmail.com", "edad": 30},
    {id: 4, "nombre": "Laura", "correo": "laura@hotmail.com", "edad": 22},
]


def buscar_por_Letra(letra, lista):
    persona = list(filter(lambda x: x["nombre"][0] == letra.upper(), lista))
    return persona


resultado = buscar_por_Letra("l", personas)
print(resultado)
