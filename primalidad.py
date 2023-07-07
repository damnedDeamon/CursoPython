# Verificar si un número es primo utilizando un enfoque básico:
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

print(es_primo(7))  # Imprime True
print(es_primo(12))  # Imprime False


# Verificar si un número es primo utilizando un enfoque optimizado:
import math

def es_primo(numero):
    if numero <= 1:
        return False
    if numero == 2 or numero == 3:
        return True
    if numero % 2 == 0:
        return False
    limite = math.isqrt(numero) + 1
    for i in range(3, limite, 2):
        if numero % i == 0:
            return False
    return True

print(es_primo(17))  # Imprime True
print(es_primo(25))  # Imprime False
# En el primer ejemplo, la función es_primo verifica si un número dado es primo al iterar desde 2 hasta el número-1 
# y comprobar si hay algún divisor que divida al número de manera exacta.