# Ejercicios
# Dado un número detectar si es positivo, negativo o cero
# Usar  operador ternario


def detectar(num):
    resultado = "Positivo" if num > 0 else ("Negativo" if num < 0 else "Es igual a cero")
    return resultado



numero = int(input("Ibgrese número: "))
try:
    result = detectar(numero)
    print(result)
except TypeError as err:
    raise TypeError(err)