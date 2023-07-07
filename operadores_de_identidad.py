# Operador "is":
a = [1, 2, 3]
b = a
print(b is a)  # True
# En este ejemplo, se compara si las variables 'a' y 'b' hacen referencia al mismo objeto en la memoria.


# Operador "is not":
a = [1, 2, 3]
b = [1, 2, 3]
print(b is not a)  # True
# Aquí se compara si las variables 'a' y 'b' no hacen referencia al mismo objeto en la memoria.


# Utilizando la función "id()":
a = [1, 2, 3]
b = [1, 2, 3]
print(id(a) == id(b))  # False
# En este ejemplo, se utiliza la función "id()" para obtener el identificador único de cada objeto y luego se compara si son iguales.