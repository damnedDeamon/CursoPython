# Ejemplo básico de bucle "while":
contador = 0

while contador < 5:
    print(contador)
    contador += 1
# En este ejemplo, el bucle "while" se ejecutará mientras el contador sea menor que 5. 
# En cada iteración, se imprimirá el valor actual del contador y luego se incrementará en 1.



# Ejemplo de bucle "while" con condición más compleja:
numero = 100

while numero > 0 and numero % 7 != 0:
    print(numero)
    numero -= 1
# En este caso, el bucle "while" se ejecutará mientras el número sea mayor que 0 y no sea divisible por 7. 
# En cada iteración, se imprimirá el número actual y se reducirá en 1.



# Ejemplo de bucle "while" con interacción del usuario:
respuesta = ""

while respuesta != "salir":
    respuesta = input("Ingresa un valor ('salir' para terminar): ")
    print("Tu respuesta fue:", respuesta)
# En este ejemplo, el bucle "while" se ejecutará mientras la respuesta del usuario no sea igual a "salir".
#  En cada iteración, se solicitará al usuario que ingrese un valor y se mostrará el valor ingresado.