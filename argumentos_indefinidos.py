# Función con argumentos arbitrarios posicionales (*args):
def sumar(*args):
    resultado = sum(args)
    return resultado

print(sumar(1, 2, 3, 4))  # Suma los argumentos: 1 + 2 + 3 + 4 = 10
print(sumar(5, 10, 15))  # Suma los argumentos: 5 + 10 + 15 = 30


# Función con argumentos arbitrarios de palabras clave (**kwargs):
def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(clave + ": " + str(valor))

mostrar_info(nombre="Juan", edad=25, pais="México")
# Imprime:
# nombre: Juan
# edad: 25
# pais: México


# Función con argumentos arbitrarios posicionales y de palabras clave combinados:
def mostrar_datos(*args, **kwargs):
    for arg in args:
        print(arg)
    for clave, valor in kwargs.items():
        print(clave + ": " + str(valor))

mostrar_datos("Juan", 25, pais="México", profesion="Ingeniero")
# Imprime:
# Juan
# 25
# pais: México
# profesion: Ingeniero