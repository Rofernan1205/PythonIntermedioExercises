# Crea una clase Producto que solo permita los atributos: nombre, precio y stock
# Intenta crear un objeto con esos atributos y luego agrega uno nuevo llamado 'categoria'.
# ¿Qué pasa?
from generadores.convertirLetras import nombre


class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock =stock


import sys
producto_1 = Producto("Soda", 11, 2)
producto_1.descripcion = "vacio"
print(producto_1.__dict__)

print(sys.getsizeof(producto_1))

class Producto2:
    __slots__= ["nombre", "precio", "stock"]
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.nombre} - {self.precio} {self.stock}"



producto_2 = Producto2("Licor", 18, 4)
print(producto_2)

print(sys.getsizeof(producto_2))

