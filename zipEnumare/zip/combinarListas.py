# Usar Zip para imprimir la listas de la siguiente manera
# Ana tiene 25 años
# Luis tiene 30 años
# Carlos tiene 28 años


nombres = ["Ana", "Luis", "Carlos"]
edades = [25, 30, 28]

lista = [x for x in zip(nombres, edades)]
print(lista)