# Verificar si una palabra es un palíndromo:
def es_palindromo(palabra):
    palabra = palabra.lower()  # Convertir a minúsculas para ignorar mayúsculas
    reverso = palabra[::-1]  # Obtener la versión invertida de la palabra
    if palabra == reverso:
        return True
    else:
        return False

print(es_palindromo("reconocer"))  # Imprime True
print(es_palindromo("python"))  # Imprime False


# Verificar si una frase es un palíndromo (ignorando espacios y signos de puntuación):
import re

def es_palindromo(frase):
    frase = re.sub(r"\W+", "", frase.lower())  # Eliminar espacios y signos de puntuación
    reverso = frase[::-1]  # Obtener la versión invertida de la frase
    if frase == reverso:
        return True
    else:
        return False

print(es_palindromo("Anita lava la tina."))  # Imprime True
print(es_palindromo("Python es divertido."))  # Imprime False

# En el primer ejemplo, la función es_palindromo verifica si una palabra dada es un palíndromo al compararla con su versión invertida.