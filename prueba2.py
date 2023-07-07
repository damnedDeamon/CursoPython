def sumar(n1 ,n2):
    result = n1 + n2
    return result

nombre = input("Hola, ¿cuál es tu nombre? ")
print("Hola " + nombre + "!")
edad_valida = False
while not edad_valida:
    try:
        edad = int(input("¿Me podrías decir cuál es tu edad? "))
        edad_valida = True
    except ValueError:
        print("Por favor, ingresa solo el número entero para tu edad.")

decada = 10
print("Estimado " + nombre + ", en una decada su edad sera de " + str(sumar(edad, decada)) + " años.")

input("Presiona enter para salir...")