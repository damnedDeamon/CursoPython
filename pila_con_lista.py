# Crear una pila vacía:
pila = []


# Verificar si la pila está vacía:
if not pila:
    print("La pila está vacía")


# Agregar elementos a la pila (push):
pila.append(1)
pila.append(2)
pila.append(3)


# Eliminar el elemento superior de la pila (pop):
elemento = pila.pop()
print("Elemento eliminado:", elemento)


# Obtener el elemento superior de la pila sin eliminarlo:
elemento_superior = pila[-1]
print("Elemento superior:", elemento_superior)


# Verificar si la pila está vacía después de eliminar elementos:
if not pila:
    print("La pila está vacía")
# Estos son solo algunos ejemplos de cómo utilizar una lista para implementar una pila en Python. 
# Puedes combinar estas operaciones básicas para realizar diferentes manipulaciones y mantener un seguimiento de los elementos en la pila.