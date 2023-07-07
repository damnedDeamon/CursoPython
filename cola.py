# rear una cola vacía:
cola = []

# Verificar si la cola está vacía:
if not cola:
    print("La cola está vacía")

# Agregar elementos a la cola (enqueue):
cola.append(1)
cola.append(2)
cola.append(3)

# Eliminar el elemento frontal de la cola (dequeue):
elemento = cola.pop(0)
print("Elemento eliminado:", elemento)

# Obtener el elemento frontal de la cola sin eliminarlo:
elemento_frontal = cola[0]
print("Elemento frontal:", elemento_frontal)

# Verificar si la cola está vacía después de eliminar elementos:
if not cola:
    print("La cola está vacía")
# Estos son solo algunos ejemplos de cómo utilizar una lista para implementar una cola en Python. 
# Puedes combinar estas operaciones básicas para realizar diferentes manipulaciones y mantener un seguimiento de los elementos en la cola.

