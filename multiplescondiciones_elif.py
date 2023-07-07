# Ejemplo de múltiples condiciones "elif" con números:
numero = 5

if numero == 0:
    print("El número es cero")
elif numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
# En este ejemplo, se verifica si el número es cero y se muestra el mensaje correspondiente. 
# Si no es cero, se verifica si el número es mayor que cero y se muestra el mensaje "El número es positivo". 
# Si ninguna de las condiciones anteriores se cumple, se asume que el número es negativo y se muestra el mensaje "El número es negativo".



# Ejemplo de múltiples condiciones "elif" con variables de texto:
pais = "México"

if pais == "España":
    print("El idioma es español")
elif pais == "México":
    print("El idioma es español")
elif pais == "Francia":
    print("El idioma es francés")
else:
    print("El idioma es desconocido")
# En este caso, se verifica el valor de la variable "pais" y se muestra el idioma correspondiente. 
# Tanto para "España" como para "México", se imprime el mensaje "El idioma es español", ya que ambos países comparten el mismo idioma. 
# Si la variable "pais" no coincide con ninguna de las condiciones anteriores, se muestra el mensaje "El idioma es desconocido".