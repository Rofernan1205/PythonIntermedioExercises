# Realizar cambio de configuracion global

# modo_oscuro = False
#
#
# def activar_modo_oscuro():
#     global modo_oscuro
#     modo_oscuro = True
#
#
# activar_modo_oscuro()
# print(modo_oscuro)  # Esperado: True

modo_oscuro = False


def activar_modo_oscuro():
    return True


modo_oscuro = activar_modo_oscuro()
print(modo_oscuro)
