# Importar el módulo math:
import math
#Utilizar la constante matemática pi:

print(math.pi)  # Imprime el valor de pi (3.141592653589793)
# Calcular la raíz cuadrada de un número:

numero = 16
raiz_cuadrada = math.sqrt(numero)
print(raiz_cuadrada)  # Imprime 4.0



# Calcular el seno, coseno y tangente de un ángulo (en radianes):
angulo_radianes = math.radians(45)  # Convertir ángulo a radianes
seno = math.sin(angulo_radianes)
coseno = math.cos(angulo_radianes)
tangente = math.tan(angulo_radianes)
print(seno, coseno, tangente)  # Imprime los valores de seno, coseno y tangente del ángulo



# Calcular el factorial de un número:
numero = 5
factorial = math.factorial(numero)
print(factorial)  # Imprime 120



# Redondear un número:
numero = 3.7
redondeado = math.ceil(numero)  # Redondeo hacia arriba
print(redondeado)  # Imprime 4

redondeado = math.floor(numero)  # Redondeo hacia abajo
print(redondeado)  # Imprime 3