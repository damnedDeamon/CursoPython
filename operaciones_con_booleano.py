# Operaciones lógicas con booleanos:
a = True
b = False


# Operador "and" (y lógico)
resultado_and = a and b
print(resultado_and)  # False


# Operador "or" (o lógico)
resultado_or = a or b
print(resultado_or)  # True


# Operador "not" (negación lógica)
resultado_not = not a
print(resultado_not)  # False
# En este ejemplo, se realizan operaciones lógicas utilizando los operadores "and", "or" y "not" con variables booleanas.


# Conversión de otros tipos de datos a booleanos:
# Enteros
num = 0
booleano = bool(num)
print(booleano)  # False


# Cadenas de texto
texto = ""
booleano = bool(texto)
print(booleano)  # False


# Listas
lista = []
booleano = bool(lista)
print(booleano)  # False


# Valores no vacíos
valor = "Hola"
booleano = bool(valor)
print(booleano)  # True
# quí se demuestra cómo se puede convertir diferentes tipos de datos a booleanos utilizando la función bool(). 
# Los valores vacíos, como cero, una cadena vacía o una lista vacía, se consideran False, mientras que los valores no vacíos se consideran True.

