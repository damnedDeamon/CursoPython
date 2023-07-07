# Ejemplo de bucle "for" con una lista:
frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    print(fruta)
# En este ejemplo, el bucle "for" se ejecutará para cada elemento de la lista "frutas". En cada iteración, se imprimirá el valor del elemento.



# Ejemplo de bucle "for" con una cadena de texto:
nombre = "Juan"

for letra in nombre:
    print(letra)
# En este caso, el bucle "for" recorrerá cada letra de la cadena de texto "nombre". En cada iteración, se imprimirá la letra.



# Ejemplo de bucle "for" con la función range():
for numero in range(1, 6):
    print(numero)
# En este ejemplo, el bucle "for" utiliza la función "range()" para generar una secuencia de números del 1 al 5. En cada iteración, se imprimirá el número correspondiente.




# Ejemplo de bucle "for" con una tupla y desempaquetado de elementos:
puntos = [(1, 2), (3, 4), (5, 6)]

for x, y in puntos:
    print("Coordenadas:", x, y)
# En este caso, el bucle "for" se utilizará para iterar sobre una lista de tuplas que representan puntos.
#  Mediante el desempaquetado de elementos, se asigna cada componente x e y de la tupla a las variables correspondientes.