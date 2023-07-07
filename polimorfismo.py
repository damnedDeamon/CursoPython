# Ejemplo 1: Polimorfismo con métodos

class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "Guau!"

class Gato(Animal):
    def hablar(self):
        return "¡Miau!"

class Vaca(Animal):
    def hablar(self):
        return "Muu!"

# Crear una lista de animales
animales = [Perro(), Gato(), Vaca()]

# Llamar al método hablar() para cada animal
for animal in animales:
    print(animal.hablar())

# En este ejemplo, las clases Perro, Gato y Vaca heredan de la clase Animal y cada una implementa su propio método hablar(). 
# Al crear una lista de objetos de diferentes clases y llamar al método hablar() para cada objeto, 
# cada objeto responde de manera diferente según su propia implementación del método. Esto es un ejemplo de polimorfismo, 
# ya que diferentes objetos de clases diferentes pueden responder de manera distinta a la misma llamada de método.




# Ejemplo 2: Polimorfismo con funciones

class Rectangulo:
    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura

    def area(self):
        return self.ancho * self.altura

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return 0.5 * self.base * self.altura

def calcular_area(figura):
    return figura.area()

# Crear objetos de diferentes clases y llamar a la función calcular_area()
rectangulo = Rectangulo(5, 3)
triangulo = Triangulo(4, 6)

print(calcular_area(rectangulo))  # Salida: 15
print(calcular_area(triangulo))   # Salida: 12

# En este ejemplo, las clases Rectangulo y Triangulo tienen un método area() que calcula el área de la figura correspondiente. La función calcular_area() 
# toma un objeto de cualquier clase que tenga un método area() y llama a ese método para calcular el área de la figura. Esto demuestra el polimorfismo, 
# ya que diferentes objetos de diferentes clases pueden ser pasados a la misma función y responder a la llamada del método de manera adecuada.