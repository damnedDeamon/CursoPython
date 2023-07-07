# Ejemplo 1: Encapsulación básica

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def get_edad(self):
        return self._edad

    def set_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self._edad = nueva_edad

# Crear un objeto de la clase Persona
persona1 = Persona("Juan", 25)

# Acceder a los atributos utilizando los métodos getter
print(persona1.get_nombre())  # Salida: Juan
print(persona1.get_edad())    # Salida: 25

# Modificar los atributos utilizando los métodos setter
persona1.set_nombre("Pedro")
persona1.set_edad(30)

print(persona1.get_nombre())  # Salida: Pedro
print(persona1.get_edad())    # Salida: 30
# En este ejemplo, la clase Persona tiene dos atributos _nombre y _edad, que están marcados como protegidos utilizando un solo guion bajo al inicio. 
# La clase también tiene métodos get_nombre(), set_nombre(), get_edad() y set_edad() para acceder y modificar los atributos. 
# Al utilizar estos métodos, podemos controlar el acceso y asegurar que los valores asignados a los atributos sean válidos 
# (por ejemplo, la edad no puede ser un número negativo).



# Ejemplo 2: Encapsulación con atributos privados

class Coche:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    def get_marca(self):
        return self.__marca

    def set_marca(self, nueva_marca):
        self.__marca = nueva_marca

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, nuevo_modelo):
        self.__modelo = nuevo_modelo

# Crear un objeto de la clase Coche
coche1 = Coche("Ford", "Mustang")

# Acceder a los atributos utilizando los métodos getter
print(coche1.get_marca())   # Salida: Ford
print(coche1.get_modelo())  # Salida: Mustang

# Modificar los atributos utilizando los métodos setter
coche1.set_marca("Tesla")
coche1.set_modelo("Model S")

print(coche1.get_marca())   # Salida: Tesla
print(coche1.get_modelo())  # Salida: Model S

# Intentar acceder directamente a los atributos privados generará un error
# print(coche1.__marca)  # Genera un AttributeError

# En este ejemplo, la clase Coche tiene dos atributos __marca y __modelo, que están marcados como privados utilizando dos guiones bajos al inicio. La clase también tiene métodos get_marca(), set_marca(), get_modelo() y set_modelo() para acceder y modificar los atributos. Al utilizar estos métodos, podemos controlar el acceso a los atributos y evitar el acceso directo desde fuera de la clase. Intentar acceder directamente a los atributos privados generará un error.