# Ejercicio
# Dado dos listas con nombres verificar cuales estan en ambas listas y mostrar en una lista nueva

grupo1 = ['Ana', 'Luis', 'Carlos']
grupo2 = ['Luis', 'Pedro', 'Ana']


def elementos_conjunto(conjunto1, conjunto2):
    duplicados = (set(conjunto1) & set(conjunto2))
    return duplicados


resultado = elementos_conjunto(grupo1, grupo2)
print(resultado)
