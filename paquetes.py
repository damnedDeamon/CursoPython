# Crea una estructura de directorios para tu paquete. Por ejemplo, puedes tener la siguiente estructura de directorios:

# mi_paquete/
#     __init__.py
#     modulo1.py
#     modulo2.py
# Dentro del archivo __init__.py, puedes agregar código de inicialización del paquete si es necesario. Este archivo también permite que Python reconozca la carpeta como un paquete.



# Define tus módulos en archivos separados dentro del paquete. Por ejemplo, en modulo1.py, puedes tener el siguiente código:
def saludar():
    print("¡Hola desde el módulo 1!")
# En modulo2.py, puedes tener el siguiente código:

def despedir():
    print("¡Adiós desde el módulo 2!")



# Ahora, puedes utilizar el paquete y sus módulos desde otro archivo Python. Por ejemplo, puedes tener un archivo llamado main.py en el mismo nivel que la carpeta mi_paquete, y utilizar el paquete de esta manera:
from mi_paquete import modulo1, modulo2

modulo1.saludar()
modulo2.despedir()

# Al ejecutar el archivo main.py, verás los mensajes de saludo y despedida impresos en la salida.