# Formateo básico con el operador %:
nombre = "Juan"
edad = 30
mensaje = "Hola, soy %s y tengo %d años." % (nombre, edad)
print(mensaje)
# En este ejemplo, utilizamos el operador % para insertar valores en una cadena de formato. 
# %s se utiliza para representar una cadena (nombre en este caso) y %d se utiliza para representar un número entero (edad en este caso).



# Formateo con el método format():
nombre = "Ana"
edad = 25
mensaje = "Hola, soy {} y tengo {} años.".format(nombre, edad)
print(mensaje)
# Aquí, utilizamos el método format() para formatear una cadena. Las llaves {} actúan como marcadores de posición para los valores a ser insertados. 
# Los valores se pasan a format() en el mismo orden en el que aparecen en la cadena.



# Formateo con f-strings (disponible a partir de Python 3.6):
nombre = "Pedro"
edad = 35
mensaje = f"Hola, soy {nombre} y tengo {edad} años."
print(mensaje)
# En este ejemplo, utilizamos f-strings, una sintaxis especial que nos permite insertar directamente expresiones y variables dentro de una cadena. 
# Las variables se colocan dentro de llaves {} precedidas por el prefijo f.



# Formateo numérico con especificadores de formato:
numero = 3.14159
resultado = "El número es {:.2f}".format(numero)
print(resultado)
# Aquí, utilizamos el especificador de formato :.2f para redondear el número a dos decimales y dar formato a la salida.