# Función para sumar dos números y retornar el resultado:
def suma(a, b):
    resultado = a + b
    return resultado

resultado_suma = suma(3, 4)
print(resultado_suma)  # Imprime 7


# Función para calcular el área de un círculo y retornar el resultado:
import math

def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return area

resultado_area = calcular_area_circulo(5)
print(resultado_area)  # Imprime aproximadamente 78.53981633974483


# Función para verificar si un número es par y retornar un valor booleano:
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

resultado_par = es_par(6)
print(resultado_par)  # Imprime True


# Función para obtener la longitud de una cadena y retornar el resultado:
def obtener_longitud(cadena):
    longitud = len(cadena)
    return longitud

resultado_longitud = obtener_longitud("Hola, mundo!")
print(resultado_longitud)  # Imprime 12


# Función para buscar el elemento máximo en una lista y retornar el valor:
def encontrar_maximo(lista):
    maximo = max(lista)
    return maximo

numeros = [4, 7, 2, 9, 5]
resultado_maximo = encontrar_maximo(numeros)
print(resultado_maximo)  # Imprime 9