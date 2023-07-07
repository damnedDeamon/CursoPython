# Cadena de caracteres simple:
mensaje = "¡Hola, mundo!"


# Concatenación de cadenas:
nombre = "Juan"
saludo = "¡Hola, " + nombre + "!"


# Indexación de caracteres:
fruta = "manzana"
primera_letra = fruta[0]
ultima_letra = fruta[-1]


# Subcadenas:
texto = "Python es genial"
subcadena = texto[7:9]  # Obtiene "es"


# Longitud de una cadena:
mensaje = "Hola"
longitud = len(mensaje)


# Búsqueda de una subcadena:
frase = "El perro marrón"
busqueda = frase.find("perro")


# Reemplazo de caracteres:
mensaje = "Hola, mundo"
nuevo_mensaje = mensaje.replace("mundo", "Python")


# Conversión de mayúsculas y minúsculas:
texto = "Python"
texto_mayusculas = texto.upper()
texto_minusculas = texto.lower()


# División de una cadena en una lista:
frase = "Hola, cómo estás?"
palabras = frase.split(",")


# Concatenar dos cadenas de texto:
nombre = "Juan"
apellido = "Pérez"
nombre_completo = nombre + " " + apellido
print(nombre_completo)  # Imprime: Juan Pérez


#Concatenar una cadena de texto con un número entero:
edad = 25
mensaje = "Tienes " + str(edad) + " años"
print(mensaje)  # Imprime: Tienes 25 años


# Concatenar una cadena de texto con un número decimal:
precio = 9.99
mensaje = "El precio es: $" + str(precio)
print(mensaje)  # Imprime: El precio es: $9.99


#Concatenar elementos de una lista en una cadena:
numeros = [1, 2, 3, 4, 5]
cadena_numeros = " ".join(str(num) for num in numeros)
print(cadena_numeros)  # Imprime: 1 2 3 4 5


#Concatenar elementos de una lista de cadenas:
palabras = ["Hola", "mundo", "!"]
oracion = " ".join(palabras)
print(oracion)  # Imprime: Hola mundo !