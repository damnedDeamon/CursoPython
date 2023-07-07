import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

longitud = 8  # Longitud de la contraseña
contrasena_generada = generar_contrasena(longitud)
print(contrasena_generada)


# En este ejemplo, utilizamos la función generar_contrasena para generar una contraseña aleatoria. 
# La función recibe un parámetro longitud que indica la cantidad de caracteres que tendrá la contraseña.

# Dentro de la función, creamos una variable caracteres que contiene todos los caracteres posibles que se pueden incluir en la contraseña. 
# En este caso, utilizamos letras (mayúsculas y minúsculas), dígitos y signos de puntuación.

# Luego, utilizamos un bucle para elegir caracteres aleatorios de caracteres y concatenarlos para formar la contraseña. 
# La función random.choice() elige un carácter aleatorio de la lista caracteres.

# Finalmente, retornamos la contraseña generada.