# 1.- # Dado 3 números, devolver los números en orden ascendente.

# En Python, puedes utilizar la función sorted() para ordenar los números en orden ascendente. Aquí tienes un ejemplo de cómo puedes hacerlo:

num1 = 10
num2 = 5
num3 = 8

numeros_ordenados = sorted([num1, num2, num3])

print(numeros_ordenados)
# Este código tomará los números num1, num2 y num3 y los colocará en una lista. Luego, 
# la función sorted() ordenará los números de forma ascendente y los asignará a la variable numeros_ordenados. 
# Finalmente, se imprimirá la lista numeros_ordenados, que contendrá los números en orden ascendente.

# La salida será: [5, 8, 10].



# 2.- # Dado un rango de números enteros, obtener la cantidad de números enteros que contiene.

# Para obtener la cantidad de números enteros en un rango determinado, 
# puedes utilizar la función range() junto con la función len() para calcular la longitud del rango. Aquí tienes un ejemplo:

inicio = 1
fin = 10

rango = range(inicio, fin + 1)  # El "+1" es para incluir el número final en el rango
cantidad_enteros = len(rango)

print(cantidad_enteros)
# En este código, se define el inicio y el fin del rango (en este caso, desde 1 hasta 10). 
# Luego, se utiliza la función range() para generar el rango de números enteros, y se guarda en la variable rango.
# Por último, se utiliza la función len() para obtener la longitud del rango, es decir, la cantidad de números enteros que contiene. El resultado se imprime en pantalla.

# La salida será: 10, ya que el rango incluye los números enteros desde 1 hasta 10, ambos inclusive.

# ============================================================================================================================================
# ============================================================================================================================================
# ============================================================================================================================================


# 3.- # Dado un rango de números enteros num. inicial y num. final, obtener la cantidad de números positivos y negativos que existen en el rango.

# Para obtener la cantidad de números positivos y negativos en un rango de números enteros, 
# puedes utilizar un bucle for junto con una estructura condicional para contar los números según su signo. Aquí tienes un ejemplo:

num_inicial = -5
num_final = 5

cant_positivos = 0
cant_negativos = 0

for num in range(num_inicial, num_final + 1):
    if num > 0:
        cant_positivos += 1
    elif num < 0:
        cant_negativos += 1

print("Cantidad de números positivos:", cant_positivos)
print("Cantidad de números negativos:", cant_negativos)


# En este código, se utiliza un bucle for para iterar sobre cada número en el rango, desde num_inicial hasta num_final (ambos inclusive). 
# Dentro del bucle, se evalúa si el número es positivo o negativo utilizando una estructura condicional (if-elif). 
# Dependiendo del caso, se incrementa el contador correspondiente (cant_positivos o cant_negativos).

# Al finalizar el bucle, se imprime la cantidad de números positivos y negativos obtenidos.

# Esto indica que en el rango de números desde -5 hasta 5 (ambos inclusive) hay 5 números positivos y 5 números negativos.