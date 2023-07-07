# lower(): Convierte una cadena a minúsculas.
cadena = "Hola, Mundo!"
resultado = cadena.lower()
print(resultado)  # Imprime "hola, mundo!"


# upper(): Convierte una cadena a mayúsculas.
cadena = "Hola, Mundo!"
resultado = cadena.upper()
print(resultado)  # Imprime "HOLA, MUNDO!"


# capitalize(): Convierte el primer carácter de una cadena a mayúscula y los demás a minúsculas.
cadena = "hola, mundo!"
resultado = cadena.capitalize()
print(resultado)  # Imprime "Hola, mundo!"


# count(): Cuenta el número de ocurrencias de una subcadena en una cadena.
cadena = "Hola, Hola, Hola!"
ocurrencias = cadena.count("Hola")
print(ocurrencias)  # Imprime 3


# replace(): Reemplaza todas las ocurrencias de una subcadena por otra en una cadena.
cadena = "Hola, mundo!"
nueva_cadena = cadena.replace("Hola", "Adiós")
print(nueva_cadena)  # Imprime "Adiós, mundo!"


# split(): Divide una cadena en una lista de subcadenas utilizando un delimitador.
cadena = "Hola, mundo!"
subcadenas = cadena.split(", ")
print(subcadenas)  # Imprime ['Hola', 'mundo!']


# join(): Une una lista de subcadenas en una sola cadena utilizando un delimitador.
subcadenas = ['Hola', 'mundo!']
cadena = ", ".join(subcadenas)
print(cadena)  # Imprime "Hola, mundo!"