# Ejemplo 1: Herencia múltiple básica

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo.")

class Mascota:
    def __init__(self, nombre, dueño):
        self.nombre = nombre
        self.dueño = dueño

    def mostrar_detalles(self):
        print(f"{self.nombre} es la mascota de {self.dueño}.")

class Perro(Animal, Mascota):
    def __init__(self, nombre, dueño, raza):
        Animal.__init__(self, nombre)
        Mascota.__init__(self, nombre, dueño)
        self.raza = raza

# Crear un objeto de la clase Perro
perro1 = Perro("Firulais", "Juan", "Labrador")

# Acceder a los atributos y métodos heredados de las clases Animal y Mascota
print(perro1.nombre)        # Salida: Firulais
perro1.comer()              # Salida: Firulais está comiendo.
perro1.mostrar_detalles()   # Salida: Firulais es la mascota de Juan.

# En este ejemplo, la clase Animal tiene un constructor __init__() y un método comer(), 
# mientras que la clase Mascota tiene un constructor __init__() y un método mostrar_detalles(). 
# La clase Perro hereda de las clases Animal y Mascota utilizando herencia múltiple. 
# Para inicializar los atributos de ambas clases padres en la clase hija, 
# se llama explícitamente a los constructores de las clases padres utilizando la sintaxis ClasePadre.__init__(self, args). 
# Luego, se pueden acceder a los atributos y métodos heredados de ambas clases padres en la clase hija.




# Ejemplo 2: Herencia múltiple con métodos con el mismo nombre

class Vehiculo:
    def desplazamiento(self):
        print("El vehículo se desplaza sobre ruedas.")

class Barco:
    def desplazamiento(self):
        print("El barco se desplaza sobre el agua.")

class Anfibio(Vehiculo, Barco):
    pass

# Crear un objeto de la clase Anfibio
anfibio1 = Anfibio()

# Llamar al método desplazamiento(), que tiene el mismo nombre en ambas clases padres
anfibio1.desplazamiento()  # Salida: El vehículo se desplaza sobre ruedas.

# En este ejemplo, la clase Vehiculo tiene un método desplazamiento() que imprime un mensaje sobre cómo se desplaza un vehículo sobre ruedas, 
# mientras que la clase Barco tiene un método desplazamiento() que imprime un mensaje sobre cómo se desplaza un barco sobre el agua. 
# La clase Anfibio hereda de ambas clases utilizando herencia múltiple y no define ningún método propio. 
# Al llamar al método desplazamiento() en un objeto de la clase Anfibio, se ejecuta el método de la primera clase padre especificada en la herencia múltiple 
# (Vehiculo en este caso).