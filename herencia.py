# Ejemplo 1: Herencia básica
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo.")

class Perro(Animal):
    def ladrar(self):
        print(f"{self.nombre} está ladrando.")

# Crear un objeto de la clase Perro
perro1 = Perro("Firulais")

# Acceder a los atributos y métodos de la clase Animal (clase padre)
print(perro1.nombre)  # Salida: Firulais
perro1.comer()        # Salida: Firulais está comiendo.

# Acceder al método propio de la clase Perro
perro1.ladrar()       # Salida: Firulais está ladrando.

# En este ejemplo, la clase Animal es la clase padre y tiene un atributo nombre y un método comer(). 
# La clase Perro es una clase hija que hereda de la clase Animal y agrega su propio método ladrar(). 
# Al crear un objeto de la clase Perro, se pueden acceder tanto a los atributos y métodos heredados de la clase Animal como a los métodos propios de la clase Perro.



# Ejemplo 2: Herencia múltiple
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def conducir(self):
        print(f"Conduciendo un vehículo de la marca {self.marca}.")

class Electrico:
    def cargar(self):
        print("Cargando el vehículo eléctrico.")

class CocheElectrico(Vehiculo, Electrico):
    def __init__(self, marca):
        super().__init__(marca)

# Crear un objeto de la clase CocheElectrico
coche1 = CocheElectrico("Tesla")

# Acceder a los atributos y métodos de las clases Vehiculo y Electrico (clases padres)
print(coche1.marca)  # Salida: Tesla
coche1.conducir()    # Salida: Conduciendo un vehículo de la marca Tesla.
coche1.cargar()      # Salida: Cargando el vehículo eléctrico.

# En este ejemplo, la clase Vehiculo tiene un atributo marca y un método conducir(), y la clase Electrico tiene un método cargar(). 
# La clase CocheElectrico es una clase hija que hereda tanto de la clase Vehiculo como de la clase Electrico utilizando la herencia múltiple. 
# Al crear un objeto de la clase CocheElectrico, se pueden acceder a los atributos y métodos de ambas clases padres.