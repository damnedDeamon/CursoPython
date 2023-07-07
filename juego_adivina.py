import random

def jugar_adivina():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido al juego de adivinanzas!")
    print("Estoy pensando en un número del 1 al 100. ¡Adivina cuál es!")

    while True:
        intento = int(input("Introduce tu adivinanza: "))
        intentos += 1

        if intento < numero_secreto:
            print("Demasiado bajo. Intenta nuevamente.")
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta nuevamente.")
        else:
            print(f"¡Felicidades! ¡Adivinaste el número en {intentos} intentos!")
            break

jugar_adivina()


# En este juego, se genera un número secreto utilizando el módulo random en el rango del 1 al 100. 
# Luego, se le pide al jugador que introduzca un número y se comparará con el número secreto.

# El juego continuará hasta que el jugador adivine el número correcto. 
# En cada intento, se le proporcionará una pista si el número adivinado es demasiado alto o demasiado bajo.