# EJercicio
# Dada una nota entre 0 y 20, muestra "Aprovado" si la nota es >= 12.5, si no "Desaprobado"
# Usa operador ternario




def evaluar_nota(nota):
    result = "Aprobado" if 12.5 <= nota <=20 else( "Desaprobado" if 0 <= nota <12.5 else "Nota no esta en el rango 0 a 20" )
    return  result
try:
    nota = float(input("Ingrese nota : "))
    resultado = evaluar_nota(nota)
    print(resultado)
except TypeError as err:
    raise TypeError(err)

