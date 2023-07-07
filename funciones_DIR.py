# Dir en un objeto:
nombre = "Juan"
print(dir(nombre))
# En este ejemplo, utilizamos dir(nombre) para obtener una lista de los atributos y métodos disponibles en el objeto nombre, que en este caso es una cadena.



# Dir en un módulo:
import math
print(dir(math))
# Aquí, utilizamos dir(math) para obtener una lista de los atributos y funciones disponibles en el módulo math.



# Dir en una clase:
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Hola, soy", self.nombre)

persona = Persona("Ana", 25)
print(dir(persona))
# En este ejemplo, creamos una clase Persona con algunos atributos y un método. 
# Luego, utilizamos dir(persona) para obtener una lista de los atributos y métodos disponibles en la instancia de la clase persona.