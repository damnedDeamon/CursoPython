# En Python, una función es un bloque de código reutilizable que realiza una tarea específica. 
# Las funciones te permiten organizar y estructurar tu código de manera más efectiva, evitando la repetición de código y facilitando su mantenimiento.


# Definición de la función
def saludar():
    print("¡Hola, bienvenido!")

# Llamada a la función
saludar()  # Imprime: ¡Hola, bienvenido!


# ============================================================================================================================================
# ============================================================================================================================================
# ============================================================================================================================================

# Las funciones también pueden aceptar argumentos, que son valores que se pasan a la función para que los utilice en su ejecución. 
# Aquí hay un ejemplo de una función que acepta un argumento:


# Definición de la función con argumento
def saludar(nombre):
    print("¡Hola,", nombre, "! Bienvenido/a.")

# Llamada a la función con argumento
saludar("Juan")  # Imprime: ¡Hola, Juan! Bienvenido/a.


# ============================================================================================================================================
# ============================================================================================================================================
# ============================================================================================================================================


# Las funciones también pueden devolver valores utilizando la instrucción return. Aquí tienes un ejemplo:

# Definición de la función con retorno
def sumar(a, b):
    resultado = a + b
    return resultado

# Llamada a la función y almacenamiento del resultado
resultado_suma = sumar(3, 4)
print(resultado_suma)  # Imprime: 7


# ============================================================================================================================================
# ============================================================================================================================================
# ============================================================================================================================================


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Llamada a la función
resultado = factorial(5)
print(resultado)  # Imprime: 120


# En este ejemplo, hemos definido una función llamada factorial() que calcula el factorial de un número dado n. La función utiliza recursividad para realizar el cálculo.

# Si n es igual a 0, la función devuelve 1 (ya que el factorial de 0 es 1). 
# En caso contrario, la función llama a sí misma con el argumento n - 1 y multiplica n por el resultado de esa llamada recursiva.

# En la llamada factorial(5), la función se ejecuta de la siguiente manera:

# factorial(5) llama a factorial(4) y multiplica 5 por el resultado.
# factorial(4) llama a factorial(3) y multiplica 4 por el resultado.
# factorial(3) llama a factorial(2) y multiplica 3 por el resultado.
# factorial(2) llama a factorial(1) y multiplica 2 por el resultado.
# factorial(1) llama a factorial(0) y multiplica 1 por el resultado.
# factorial(0) devuelve 1.
# Entonces, la función factorial(5) devuelve 5 * 4 * 3 * 2 * 1 = 120.

# ============================================================================================================================================
# ============================================================================================================================================
# ============================================================================================================================================


# En este ejemplo se realiza la búsqueda de un elemento en una lista utilizando el algoritmo de búsqueda binaria:

def busqueda_binaria(lista, elemento):
    primero = 0
    ultimo = len(lista) - 1

    while primero <= ultimo:
        medio = (primero + ultimo) // 2
        valor_medio = lista[medio]

        if valor_medio == elemento:
            return medio
        elif valor_medio < elemento:
            primero = medio + 1
        else:
            ultimo = medio - 1

    return -1

# Lista ordenada de ejemplo
mi_lista = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

# Llamada a la función para buscar el elemento 23
resultado = busqueda_binaria(mi_lista, 23)
if resultado != -1:
    print("El elemento se encuentra en la posición:", resultado)
else:
    print("El elemento no se encuentra en la lista.")

# En este ejemplo, la función busqueda_binaria() implementa el algoritmo de búsqueda binaria para encontrar un elemento en una lista ordenada. 
# La función recibe dos parámetros: lista, que es la lista en la que se realizará la búsqueda, y elemento, que es el valor que se desea encontrar.



# Función sin parámetros ni valor de retorno:
def saludar():
    print("Hola, ¡bienvenido!")

saludar()  # Llamada a la función: Imprime "Hola, ¡bienvenido!"


# Función con parámetros:
def suma(a, b):
    resultado = a + b
    print("El resultado de la suma es:", resultado)

suma(5, 3)  # Llamada a la función: Imprime "El resultado de la suma es: 8"


# Función con valor de retorno:
def multiplicar(a, b):
    resultado = a * b
    return resultado

resultado = multiplicar(4, 6)
print("El resultado de la multiplicación es:", resultado)  # Imprime "El resultado de la multiplicación es: 24"


# Función con parámetros opcionales:
def saludar(nombre, saludo="Hola"):
    mensaje = saludo + ", " + nombre + "!"
    print(mensaje)

saludar("Juan")  # Llamada a la función: Imprime "Hola, Juan!"
saludar("Ana", "¡Hola")  # Llamada a la función: Imprime "¡Hola, Ana!"


# Función recursiva:
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

resultado = factorial(5)
print("El factorial de 5 es:", resultado)  # Imprime "El factorial de 5 es: 120"