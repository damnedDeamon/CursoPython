# Ejemplo 1: Constructor básico

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

# Crear un objeto de la clase Persona utilizando el constructor
persona1 = Persona("Juan", 25)
persona1.mostrar_informacion()

# En este ejemplo, la clase Persona tiene un constructor __init__() que toma dos parámetros: nombre y edad. 
# Dentro del constructor, se asignan estos valores a los atributos self.nombre y self.edad. Luego, se define un método mostrar_informacion() 
# para imprimir los valores de los atributos. Al crear un objeto de la clase Persona utilizando el constructor, se pasan los valores "Juan" y 25, 
# y luego se llama al método mostrar_informacion() para mostrar la información de la persona.



# Ejemplo 2: Constructor con valores por defecto

class Coche:
    def __init__(self, marca, modelo, color="Negro"):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")

# Crear un objeto de la clase Coche utilizando el constructor con valores por defecto
coche1 = Coche("Ford", "Mustang")
coche1.mostrar_informacion()

# Crear otro objeto de la clase Coche con un color personalizado
coche2 = Coche("Tesla", "Model S", "Rojo")
coche2.mostrar_informacion()

# En este ejemplo, la clase Coche tiene un constructor __init__() que toma los parámetros marca, 
# modelo y un parámetro opcional color con un valor por defecto "Negro". Dentro del constructor, 
# se asignan estos valores a los atributos self.marca, self.modelo y self.color. Se define un método mostrar_informacion() 
# para imprimir los valores de los atributos. Al crear un objeto de la clase Coche, se pueden pasar los valores de marca y modelo,
# y si se proporciona un valor adicional para color, se asignará ese valor; de lo contrario, se utilizará el valor por defecto.