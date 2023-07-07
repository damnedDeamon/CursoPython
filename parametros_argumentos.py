# Función con un parámetro:
def saludar(nombre):
    print("Hola, " + nombre + "!")

saludar("Juan")  # "Juan" es el argumento pasado al parámetro "nombre"


# Función con múltiples parámetros:
def sumar(a, b):
    resultado = a + b
    print("La suma de", a, "y", b, "es:", resultado)

sumar(3, 4)  # 3 y 4 son los argumentos pasados a los parámetros "a" y "b"


# Función con parámetros predeterminados:
def saludar(nombre, saludo="Hola"):
    print(saludo + ", " + nombre + "!")

saludar("Juan")  # "Juan" es el argumento para el parámetro "nombre", el saludo será "Hola" (valor predeterminado)
saludar("Ana", "¡Hola")  # "Ana" es el argumento para el parámetro "nombre", el saludo será "¡Hola"


# Función con número variable de argumentos (argumentos arbitrarios):
def listar_nombres(*nombres):
    for nombre in nombres:
        print(nombre)

listar_nombres("Juan", "Ana", "Pedro")  # "Juan", "Ana" y "Pedro" son los argumentos pasados como una secuencia



# Función con parámetros de palabras clave (keyword arguments):
def mostrar_informacion(nombre, edad):
    print("Nombre:", nombre)
    print("Edad:", edad)

mostrar_informacion(nombre="Juan", edad=25)  # Los argumentos se pasan usando palabras clave