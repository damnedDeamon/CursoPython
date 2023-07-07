# Función recursiva para calcular el factorial de un número:
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

resultado = factorial(5)
print(resultado)  # Imprime 120


# Función recursiva para calcular la serie de Fibonacci:
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

resultado = fibonacci(6)
print(resultado)  # Imprime 8


# Función recursiva para calcular la potencia de un número:
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

resultado = potencia(2, 3)
print(resultado)  # Imprime 8


# Función recursiva para imprimir los números en un rango:
def imprimir_rango(inicio, fin):
    if inicio <= fin:
        print(inicio)
        imprimir_rango(inicio + 1, fin)

imprimir_rango(1, 5)
# Imprime:
# 1
# 2
# 3
# 4
# 5