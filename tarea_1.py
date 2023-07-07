# Crear un programa para encontrar el Área de un Círculo.

import math

def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area

radio = float(input("Ingrese el radio del círculo: "))
area_circulo = calcular_area_circulo(radio)
print("El área del círculo es:", round(area_circulo,2))


# En este programa, utilizamos la fórmula del área del círculo: A = π * r^2. Primero, importamos el módulo math para acceder a la constante pi. 
# Luego, definimos una función llamada calcular_area_circulo que toma el radio como argumento y retorna el área del círculo.

# Pedimos al usuario que ingrese el radio del círculo utilizando la función input y lo convertimos a un número de punto flotante utilizando float(). 
# Luego, llamamos a la función calcular_area_circulo con el radio proporcionado por el usuario y almacenamos el resultado en la variable area_circulo.

# Finalmente, imprimimos el resultado utilizando la función print.

# ============================================================================================================================================
# ============================================================================================================================================
# ============================================================================================================================================


# Crear un programa que permita convertir una cantidad de segundos en horas, minutos y segundos.


def convertir_segundos(segundos):
    horas = segundos // 3600
    segundos_restantes = segundos % 3600
    minutos = segundos_restantes // 60
    segundos_finales = segundos_restantes % 60
    return horas, minutos, segundos_finales

# Solicitar al usuario la cantidad de segundos
segundos = int(input("Ingrese la cantidad de segundos: "))

# Llamar a la función para realizar la conversión
horas, minutos, segundos_finales = convertir_segundos(segundos)

# Imprimir el resultado
print(f"{segundos} segundos son equivalentes a: {horas} horas, {minutos} minutos y {segundos_finales} segundos.")


# Este programa define una función llamada convertir_segundos que toma como entrada la cantidad de segundos y devuelve las horas, minutos y segundos equivalentes. 
# Luego, solicita al usuario la cantidad de segundos, llama a la función convertir_segundos y muestra el resultado en la consola.