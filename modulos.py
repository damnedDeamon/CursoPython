# Crea un archivo Python con la extensión ".py". Por ejemplo, puedes llamarlo "mimodulo.py".
# En el archivo "mimodulo.py", define funciones, variables u otros elementos que deseas incluir en tu módulo. Aquí hay un ejemplo con una función:

def saludar(nombre):
    print("¡Hola, {}!".format(nombre))


# Guarda el archivo "mimodulo.py" en la misma carpeta donde tienes tu programa principal o en una ubicación accesible.
# Ahora, en tu programa principal, puedes importar el módulo que creaste y usar las funciones o variables definidas en él.

import mimodulo

mimodulo.saludar("Juan")

# En este ejemplo, el archivo "mimodulo.py" contiene la función saludar(), que imprime un saludo personalizado. 
# Luego, en el programa principal, importamos el módulo "mimodulo" y llamamos a la función saludar() pasándole un nombre como argumento.


# En este ejemplo, importamos todo el módulo "mimodulo" y utilizamos la función saludar() mediante el nombre del módulo seguido de un punto.
# Importar un elemento específico del módulo y utilizarlo directamente:
from mimodulo import saludar
saludar("Juan")


# Importar un módulo con un alias:
import mimodulo as mm
mm.saludar("Juan")


# importar todos los elementos del módulo sin utilizar el nombre del módulo:
from mimodulo import *
saludar("Juan")