# Concatenación de cadenas:
saludo = "¡Hola, "
nombre = "Juan"
mensaje = saludo + nombre + "!"
print(mensaje)  # Imprime: ¡Hola, Juan!


#Multiplicación de cadenas (repetición):
texto = "Python "
repetido = texto * 3
print(repetido)  # Imprime: Python Python Python 


#Indexación de caracteres:
fruta = "manzana"
primera_letra = fruta[0]
ultima_letra = fruta[-1]
print(primera_letra)  # Imprime: m
print(ultima_letra)  # Imprime: a


#Obtención de una subcadena:
mensaje = "¡Hola, mundo!"
subcadena = mensaje[7:12]
print(subcadena)  # Imprime: mundo


#Longitud de una cadena:
palabra = "Python"
longitud = len(palabra)
print(longitud)  # Imprime: 6


#Búsqueda de una subcadena:
frase = "El perro marrón"
busqueda = frase.find("perro")
print(busqueda)  # Imprime: 3


#Reemplazo de caracteres:
mensaje = "Hola, mundo"
nuevo_mensaje = mensaje.replace("mundo", "Python")
print(nuevo_mensaje)  # Imprime: Hola, Python


#Conversión de mayúsculas y minúsculas:
texto = "Python"
texto_mayusculas = texto.upper()
texto_minusculas = texto.lower()
print(texto_mayusculas)  # Imprime: PYTHON
print(texto_minusculas)  # Imprime: python