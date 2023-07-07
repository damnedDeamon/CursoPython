# Clase y objeto básico
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear un objeto de la clase Persona
persona1 = Persona("Juan", 25)
persona1.saludar()  # Salida: Hola, mi nombre es Juan y tengo 25 años.
# En este ejemplo, definimos una clase llamada "Persona" que tiene un constructor __init__ para inicializar los atributos nombre y edad. 
# También tenemos un método llamado saludar que muestra un mensaje de saludo utilizando los atributos del objeto. 
# Luego creamos un objeto de la clase Persona llamado "persona1" con los valores "Juan" y 25, y llamamos al método saludar() del objeto.


# Clase y objetos relacionados
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0

    def acelerar(self, incremento):
        self.velocidad += incremento

    def frenar(self, decremento):
        self.velocidad -= decremento

# Crear dos objetos de la clase Coche
coche1 = Coche("Ford", "Mustang")
coche2 = Coche("Tesla", "Model S")

coche1.acelerar(50)
print(coche1.velocidad)  # Salida: 50

coche2.acelerar(30)
coche2.frenar(10)
print(coche2.velocidad)  # Salida: 20
# En este ejemplo, definimos una clase "Coche" que tiene un constructor para inicializar los atributos marca, modelo y velocidad. 
# También tenemos métodos acelerar y frenar para modificar la velocidad del coche. 
# Creamos dos objetos de la clase Coche llamados "coche1" y "coche2" y realizamos algunas operaciones, como acelerar y frenar, en cada uno de ellos. 
# cxLuego imprimimos la velocidad de cada coche.