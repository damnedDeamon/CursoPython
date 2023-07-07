# Ingrese 6 números en una lista y obtenga el número mayor y menor ingresado.

numeros = []
for i in range(6):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

numero_mayor = max(numeros)
numero_menor = min(numeros)

print("El número mayor es:", numero_mayor)
print("El número menor es:", numero_menor)


# En este ejemplo, utilizamos un bucle for para solicitar al usuario que ingrese 6 números. 
# Cada número se convierte en un entero y se agrega a la lista numeros mediante el método append(). 
# Luego, utilizamos las funciones max() y min() para obtener el número mayor y menor, respectivamente, de la lista numeros. 
# Finalmente, mostramos los resultados utilizando la función print().