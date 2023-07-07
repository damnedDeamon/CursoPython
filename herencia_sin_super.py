# Ejemplo 1: Herencia básica sin super()

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo.")

class Perro(Animal):
    def __init__(self, nombre, raza):
        Animal.__init__(self, nombre)  # Llamada al constructor de la clase padre
        self.raza = raza

    def comer(self):
        Animal.comer(self)  # Llamada al método de la clase padre
        print("¡El perro está muy contento comiendo!")

# Crear un objeto de la clase Perro
perro1 = Perro("Firulais", "Labrador")
perro1.comer()

# En este ejemplo, la clase Perro hereda de la clase Animal, pero en lugar de utilizar super() para llamar al constructor y al método de la clase padre, 
# se utiliza la sintaxis ClasePadre.__init__(self, args) para llamar al constructor y ClasePadre.metodo(self) para llamar al método.




# Ejemplo 2: Herencia múltiple sin super()

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
        Vehiculo.__init__(self, marca)  # Llamada al constructor de la primera clase padre

# Crear un objeto de la clase CocheElectrico
coche1 = CocheElectrico("Tesla")

# Acceder a los atributos y métodos de las clases Vehiculo y Electrico (clases padres)
print(coche1.marca)  # Salida: Tesla
coche1.conducir()    # Salida: Conduciendo un vehículo de la marca Tesla.
coche1.cargar()      # Salida: Cargando el vehículo eléctrico.

# En este ejemplo, la clase CocheElectrico hereda tanto de la clase Vehiculo como de la clase Electrico, 
# pero en lugar de usar super() para llamar al constructor y métodos de las clases padres, se utiliza la sintaxis ClasePadre.__init__(self, args) y ClasePadre.metodo(self).