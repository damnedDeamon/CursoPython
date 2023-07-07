# Función lambda para sumar dos números:
suma = lambda a, b: a + b
resultado = suma(3, 4)
print(resultado)  # Imprime 7


# Función lambda para calcular el cuadrado de un número:
cuadrado = lambda x: x ** 2
resultado = cuadrado(5)
print(resultado)  # Imprime 25


# Función lambda para verificar si un número es par:
es_par = lambda num: num % 2 == 0
resultado = es_par(6)
print(resultado)  # Imprime True


# Función lambda para ordenar una lista de números de forma ascendente:
numeros = [4, 2, 6, 1, 9, 5]
numeros_ordenados = sorted(numeros, key=lambda x: x)
print(numeros_ordenados)  # Imprime [1, 2, 4, 5, 6, 9]


# Función lambda para filtrar elementos de una lista:
numeros = [1, 2, 3, 4, 5, 6]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)  # Imprime [2, 4, 6]

# Las funciones lambda son funciones anónimas que se pueden utilizar para crear funciones pequeñas y simples en una sola línea de código. 
# Son útiles cuando necesitas una función temporal o una función simple sin la necesidad de definirla formalmente con la palabra clave def.