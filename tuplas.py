# Crear una tupla:
mi_tupla = (1, 2, 3, 4, 5)


# Acceder a los elementos de una tupla:
mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla[0])  # Imprime 1
print(mi_tupla[2])  # Imprime 3


# Desempaquetar una tupla en variables individuales:
mi_tupla = ("Juan", 25, "México")
nombre, edad, pais = mi_tupla
print(nombre)  # Imprime "Juan"
print(edad)  # Imprime 25
print(pais)  # Imprime "México"


# Concatenar tuplas:
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)  # Imprime (1, 2, 3, 4, 5, 6)


# Comprobar la existencia de un elemento en una tupla:
mi_tupla = (1, 2, 3, 4, 5)
print(3 in mi_tupla)  # Imprime True
print(6 in mi_tupla)  # Imprime False


# Obtener la longitud de una tupla:
mi_tupla = (1, 2, 3, 4, 5)
print(len(mi_tupla))  # Imprime 5


# Iterar sobre una tupla:
mi_tupla = (1, 2, 3, 4, 5)
for elemento in mi_tupla:
    print(elemento)