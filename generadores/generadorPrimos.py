# Generador de números primos
# Crea un generador que produzca números primos de forma infinita (o hasta un límite si lo prefieres).

def genera_numeros_primos(limite):
    for numero in range(2, limite):
        es_primo = True
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break
        if es_primo:
            yield numero


for primo in genera_numeros_primos(10):
    print(primo)