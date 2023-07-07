# Eliminar una variable:
x = 10
print(x)  # Imprime 10

del x
print(x)  # Genera un error, ya que la variable ha sido eliminada


# Eliminar un elemento de una lista:
mi_lista = [1, 2, 3, 4, 5]
print(mi_lista)  # Imprime [1, 2, 3, 4, 5]

del mi_lista[2]
print(mi_lista)  # Imprime [1, 2, 4, 5]



# Eliminar una clave de un diccionario:
mi_diccionario = {"nombre": "Juan", "edad": 25, "pais": "México"}
print(mi_diccionario)  # Imprime {"nombre": "Juan", "edad": 25, "pais": "México"}

del mi_diccionario["edad"]
print(mi_diccionario)  # Imprime {"nombre": "Juan", "pais": "México"}



# Eliminar un elemento de un conjunto:
mi_conjunto = {1, 2, 3, 4, 5}
print(mi_conjunto)  # Imprime {1, 2, 3, 4, 5}

del mi_conjunto[2]  # Genera un error, ya que los conjuntos no son indexables



# Eliminar un atributo de un objeto:
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

juan = Persona("Juan", 25)
print(juan.nombre)  # Imprime "Juan"

del juan.nombre
print(juan.nombre)  # Genera un error, ya que el atributo ha sido eliminado