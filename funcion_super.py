# Ejemplo 1: Llamada a un método de la clase padre

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo.")

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)  # Llamada al constructor de la clase padre
        self.raza = raza

    def comer(self):
        super().comer()  # Llamada al método de la clase padre
        print("¡El perro está muy contento comiendo!")

# Crear un objeto de la clase Perro
perro1 = Perro("Firulais", "Labrador")
perro1.comer()
# En este ejemplo, la clase Animal tiene un constructor __init__() y un método comer(). 
# La clase Perro es una clase hija que hereda de la clase Animal y agrega su propio constructor __init__() y método comer(). 
# Utilizamos la función super().__init__(nombre) en el constructor de la clase Perro para llamar al constructor de la clase padre y establecer el atributo nombre. 
# Luego, utilizamos super().comer() en el método comer() de la clase Perro para llamar al método comer() de la clase padre y extender su comportamiento.



# Ejemplo 2: Llamada a un método de la clase padre con argumentos adicionales

class Figura:
    def __init__(self, color):
        self.color = color

    def mostrar_info(self):
        print(f"Figura de color {self.color}.")

class Rectangulo(Figura):
    def __init__(self, color, ancho, altura):
        super().__init__(color)  # Llamada al constructor de la clase padre
        self.ancho = ancho
        self.altura = altura

    def mostrar_info(self):
        super().mostrar_info()  # Llamada al método de la clase padre
        print(f"Rectángulo de ancho {self.ancho} y altura {self.altura}.")

# Crear un objeto de la clase Rectangulo
rectangulo1 = Rectangulo("Rojo", 5, 3)
rectangulo1.mostrar_info()
# En este ejemplo, la clase Figura tiene un constructor __init__() y un método mostrar_info(). 
# La clase Rectangulo es una clase hija que hereda de la clase Figura y agrega su propio constructor __init__() y método mostrar_info(). 
# Utilizamos super().__init__(color) en el constructor de la clase Rectangulo para llamar al constructor de la clase padre y establecer el atributo color. 
# Luego, utilizamos super().mostrar_info() en el método mostrar_info() de la clase Rectangulo para llamar al método mostrar_info() de la clase padre y extender su comportamiento.