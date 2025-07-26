# Ejercicio
# Dado tres números a, b y c, imprime el numero mayor
# Usar operador ternario

a = 2
b = 5
c = 20

def mayor_de_tres(x, y, z):
    result = x if y <= x > z else (y if x < y >= z else (z if  y < z >= x else "Son iguales"))
    return  result

resultado = mayor_de_tres(a,b,c)
print(resultado)