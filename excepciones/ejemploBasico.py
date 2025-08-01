# Ejercicio
# Desarrolle un programa que reciba un dato y que lo divida
# hacer uso de excepciones cuando se ingrese un tipo de dato que no sea de tipo
# hacer uso de excepciones en caso que se ingrese cero
# sin usar excepciones

def division_numero(num):
    return 100/num
try:
    numero = int(input("Ingrese numero : "))
    resultado = division_numero(numero)
except ZeroDivisionError as err:
    print (err)
except ValueError as err:
    print(err)
else:
    print(f"Resultado sin errores es {resultado}")
finally:
    print("final de programa")

print("salida de datos")

