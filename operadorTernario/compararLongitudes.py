# Ejercicio
# Dados dos cadenas de texto, imprime el mas largo. Si tiene
# la misma longitud , imprime Iguales

string1 = input("Ingrese cadena 1: ").strip()
string2 = input("Ingrese cadena 2: ").strip()

def comparador(s1, s2):
    resultado= s1 if  len(s1) > len(s2) else (s2 if len(s1) < len(s2) else "Son iguales")
    return resultado

salida = comparador(string1,string2)
print(salida)




