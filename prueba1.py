import tkinter as tk

def mostrar_texto(event=None):
    texto = entrada.get()
    caja_texto.insert(tk.END, texto + "\n")
    return 'break'  # Para evitar que se inserte una nueva línea al presionar Enter

# Crear la ventana principal
ventana = tk.Tk()

# Crear la caja de texto
caja_texto = tk.Text(ventana)
caja_texto.pack()

# Crear la entrada de texto
entrada = tk.Entry(ventana)
entrada.pack()

# Vincular la tecla Enter a la función mostrar_texto
entrada.bind('<Return>', mostrar_texto)

# Crear el botón
boton = tk.Button(ventana, text="Mostrar", command=mostrar_texto)
boton.pack()

# Ejecutar la ventana principal
ventana.mainloop()
