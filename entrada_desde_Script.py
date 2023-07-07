# Obtener entrada de texto desde el usuario:
nombre = input("Ingrese su nombre: ")
print("Hola, " + nombre + "!")
# En este ejemplo, utilizamos la función input() para solicitar al usuario que ingrese su nombre. 
# El texto proporcionado por el usuario se guarda en la variable nombre, y luego se imprime un saludo personalizado utilizando ese nombre.


# Obtener entrada numérica desde el usuario:
edad = int(input("Ingrese su edad: "))
año_nacimiento = 2023 - edad
print("Usted nació aproximadamente en el año", año_nacimiento)


# Aquí, utilizamos la función input() para solicitar al usuario que ingrese su edad. 
# La entrada se convierte a un número entero utilizando int(), y luego se realiza un cálculo para estimar el año de nacimiento. 
# El año de nacimiento se imprime en la salida.

# Recuerda que la función input() devuelve siempre una cadena de texto, 
# por lo que es necesario convertirlo a un tipo de dato apropiado (como un entero) si se necesita realizar operaciones matemáticas o comparaciones.



# Obtener múltiples entradas en una línea separadas por espacios:
datos = input("Ingrese varios números separados por espacios: ")
numeros = datos.split()
suma = sum([int(num) for num in numeros])
print("La suma de los números es:", suma)


# Obtener múltiples entradas en líneas separadas hasta que se ingrese un valor específico:
lineas = []
while True:
    linea = input("Ingrese una línea (o 'fin' para terminar): ")
    if linea.lower() == "fin":
        break
    lineas.append(linea)

print("Las líneas ingresadas son:")
for linea in lineas:
    print(linea)