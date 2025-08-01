#  Objetivo: Mostrar cuántas respuestas son correctas.

respuestas = ["A", "C", "B", "D"]
clave = ["A", "C", "D", "D"]

correctas = sum([r == c for r, c in zip(respuestas, clave)])
print(f"Correctas: {correctas}")
