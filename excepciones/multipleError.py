try:
    lista = [1, 2, 3]
    print(lista[5])
    print(10 / 0)
except IndexError as err:
    print(f"Índice fuera de rango {err}")
except ZeroDivisionError as err :
    print(f"División entre cero {err}")
else:
    print("Sin error")
finally:
    print("fin de programa")
