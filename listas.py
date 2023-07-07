# Creación de una lista:
numeros = [1, 2, 3, 4, 5]


# Acceso a elementos de una lista mediante indexación:
colores = ["rojo", "verde", "azul"]
primer_color = colores[0]
segundo_color = colores[1]


# Modificación de elementos de una lista:
frutas = ["manzana", "plátano", "naranja"]
frutas[1] = "pera"


# Añadir elementos a una lista:
peliculas = ["Titanic", "Avatar", "Jurassic Park"]
peliculas.append("Matrix")


# Eliminar elementos de una lista:
numeros = [1, 2, 3, 4, 5]
del numeros[2]  # Elimina el elemento en el índice 2


# Obtener la longitud de una lista:
animales = ["perro", "gato", "ratón"]
longitud = len(animales)


# Comprobar si un elemento está en una lista:
frutas = ["manzana", "plátano", "naranja"]
existe_manzana = "manzana" in frutas


# Ordenar una lista:
numeros = [3, 1, 5, 2, 4]
numeros.sort()


# Obtener una sublista (rebanado):
letras = ["a", "b", "c", "d", "e"]
sublista = letras[1:4]  # Obtiene los elementos en los índices 1, 2 y 3