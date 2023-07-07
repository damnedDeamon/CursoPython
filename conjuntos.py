# Crear un conjunto:
mi_conjunto = {1, 2, 3, 4, 5}


# Agregar elementos a un conjunto:
mi_conjunto = {1, 2, 3}
mi_conjunto.add(4)
print(mi_conjunto)  # Imprime {1, 2, 3, 4}


# Eliminar elementos de un conjunto:
mi_conjunto = {1, 2, 3, 4}
mi_conjunto.remove(3)
print(mi_conjunto)  # Imprime {1, 2, 4}


# Comprobar la existencia de un elemento en un conjunto:
mi_conjunto = {1, 2, 3, 4, 5}
print(3 in mi_conjunto)  # Imprime True
print(6 in mi_conjunto)  # Imprime False


# Operaciones de conjuntos:
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

# Unión de conjuntos
union = conjunto1.union(conjunto2)
print(union)  # Imprime {1, 2, 3, 4, 5}

# Intersección de conjuntos
interseccion = conjunto1.intersection(conjunto2)
print(interseccion)  # Imprime {3}

# Diferencia de conjuntos
diferencia = conjunto1.difference(conjunto2)
print(diferencia)  # Imprime {1, 2}

# Diferencia simétrica de conjuntos
diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
print(diferencia_simetrica)  # Imprime {1, 2, 4, 5}


# Iterar sobre un conjunto:
mi_conjunto = {1, 2, 3, 4, 5}
for elemento in mi_conjunto:
    print(elemento)