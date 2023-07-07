# Casting a entero:
numero = 10
cadena = "15"
resultado = numero + int(cadena)
print(resultado)  # Imprime: 25


# Casting a decimal:
precio = 9.99
cantidad = 2
total = precio * float(cantidad)
print(total)  # Imprime: 19.98


# Casting a cadena de caracteres:
numero = 42
cadena = "El número es: " + str(numero)
print(cadena)  # Imprime: El número es: 42


# Casting a lista:
cadena = "Hola, mundo"
lista = list(cadena)
print(lista)  # Imprime: ['H', 'o', 'l', 'a', ',', ' ', 'm', 'u', 'n', 'd', 'o']


# Casting a tupla:
lista = [1, 2, 3, 4, 5]
tupla = tuple(lista)
print(tupla)  # Imprime: (1, 2, 3, 4, 5)

"""
Estas son solo algunas de las conversiones de tipo de datos más comunes en Python. 
Puedes utilizar estas funciones de casting (int(), float(), str(), list(), tuple(), etc.) 
para convertir los datos a un tipo de dato específico según tus necesidades en tus programas. 
Recuerda que es importante realizar casting adecuado para evitar errores y asegurar que los datos se manipulen correctamente.
"""