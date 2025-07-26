# Ejercicio
# Ingrese edad de una persona y imprima
# "Niño" si < 13
# "Adolecente" si < 18
# "Adulto" si >= 18
# Usar operador ternario

def detectar_edad(edad):
    result = "Niño" if 0 < edad <13 else ( "Adolecente" if 13 <= edad < 18 else ("Adulto" if 18 <= edad <= 110  else "Año no válido" ))
    return result

try:
    edad = int(input("Ingrese edad : "))
    salida = detectar_edad(edad)
    print(salida)
except TypeError as err:
    raise TypeError(err)