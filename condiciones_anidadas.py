# Ejemplo de condiciones anidadas con if-else:
edad = 20
genero = "Femenino"

if edad >= 18:
    if genero == "Femenino":
        print("Eres una mujer mayor de edad")
    else:
        print("Eres un hombre mayor de edad")
else:
    print("Eres menor de edad")
# En este ejemplo, se evalúa la edad y, si es mayor o igual a 18, se verifica el género. 
# Dependiendo del género, se muestra un mensaje específico. Si la edad es menor a 18, se muestra el mensaje "Eres menor de edad".




# Ejemplo de condiciones anidadas con if-elif-else:
puntuacion = 75

if puntuacion >= 90:
    print("Excelente trabajo")
elif puntuacion >= 70:
    if puntuacion >= 80:
        print("Buena puntuación")
    else:
        print("Puntuación promedio")
elif puntuacion >= 50:
    print("Puntuación aceptable")
else:
    print("Debes mejorar")
# En este caso, se evalúa la puntuación y, dependiendo del rango de la puntuación, se muestran diferentes mensajes. 
# Si la puntuación está en el rango de 70 a 79, se realiza una segunda evaluación y se muestra un mensaje adicional según el valor específico.

# Las condiciones anidadas te permiten establecer una lógica más compleja y realizar diferentes comprobaciones dentro de una estructura condicional. 
# Puedes anidar múltiples niveles de condiciones para adaptar tu programa a situaciones más específicas.