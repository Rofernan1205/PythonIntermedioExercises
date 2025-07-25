# Ejercicio: Sumar solo valores numéricos de **kwargs
# Crea una función que reciba cualquier cantidad de pares clave-valor, y sume solo los valores que sean numéricos.

def sumar_valores_numericos(**kwargs):
    valores = []
    for key, value in kwargs.items():
        if isinstance(value, int):
            valores.append(value)
    return sum(valores)


resultado = sumar_valores_numericos(nombre="Rodrigo", edad=28, hijos=4, pais="Perú")

print(resultado)