# Crear un diccionario:
mi_diccionario = {"nombre": "Juan", "edad": 25, "pais": "México"}


# Acceder a los valores de un diccionario:
mi_diccionario = {"nombre": "Juan", "edad": 25, "pais": "México"}
print(mi_diccionario["nombre"])  # Imprime "Juan"
print(mi_diccionario["edad"])  # Imprime 25


# Modificar valores de un diccionario:
mi_diccionario = {"nombre": "Juan", "edad": 25, "pais": "México"}
mi_diccionario["edad"] = 30
print(mi_diccionario)  # Imprime {"nombre": "Juan", "edad": 30, "pais": "México"}


# Agregar elementos a un diccionario:
mi_diccionario = {"nombre": "Juan", "edad": 25}
mi_diccionario["pais"] = "México"
print(mi_diccionario)  # Imprime {"nombre": "Juan", "edad": 25, "pais": "México"}


# Eliminar elementos de un diccionario:
mi_diccionario = {"nombre": "Juan", "edad": 25, "pais": "México"}
del mi_diccionario["edad"]
print(mi_diccionario)  # Imprime {"nombre": "Juan", "pais": "México"}


# Comprobar la existencia de una clave en un diccionario:
mi_diccionario = {"nombre": "Juan", "edad": 25, "pais": "México"}
print("nombre" in mi_diccionario)  # Imprime True
print("profesion" in mi_diccionario)  # Imprime False


# Obtener las claves y los valores de un diccionario:
mi_diccionario = {"nombre": "Juan", "edad": 25, "pais": "México"}
claves = mi_diccionario.keys()
valores = mi_diccionario.values()
print(claves)  # Imprime ["nombre", "edad", "pais"]
print(valores)  # Imprime ["Juan", 25, "México"]