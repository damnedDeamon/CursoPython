# Ejemplo de "break" en un bucle "while":
contador = 0

while contador < 5:
    if contador == 3:
        break
    print(contador)
    contador += 1
# En este ejemplo, el bucle "while" se ejecutará hasta que el contador sea igual a 3.
# Cuando eso sucede, se encuentra la instrucción "break" que rompe el bucle y finaliza la ejecución.




# Ejemplo de "continue" en un bucle "for":
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    if numero % 2 == 0:
        continue
    print(numero)
# En este caso, el bucle "for" itera sobre la lista de números.
# Cuando encuentra un número par, la instrucción "continue" salta al siguiente iterador sin ejecutar las líneas de código restantes dentro del bucle.
# Esto significa que no se imprimirán los números pares en la salida.




# Ejemplo combinado de "break" y "continue" en un bucle "while":
contador = 0

while contador < 10:
    contador += 1
    if contador % 2 == 0:
        continue
    if contador == 7:
        break
    print(contador)
# En este ejemplo, el bucle "while" se ejecutará hasta que el contador sea igual a 7. 
# Si el contador es un número par, se utilizará "continue" para saltar a la siguiente iteración sin imprimirlo. 
# Cuando el contador alcanza el valor 7, se encuentra la instrucción "break", lo que hace que el bucle se rompa y finalice la ejecución.