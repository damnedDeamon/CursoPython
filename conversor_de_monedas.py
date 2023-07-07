def convertir_moneda(cantidad, tasa_conversion):
    return cantidad * tasa_conversion

# Tasas de conversión
tasa_dolar_euro = 0.85
tasa_dolar_libra = 0.72

# Conversión de dólares a euros
cantidad_dolares = 100
cantidad_euros = convertir_moneda(cantidad_dolares, tasa_dolar_euro)
print(cantidad_dolares, "dólares son equivalentes a", cantidad_euros, "euros.")

# Conversión de dólares a libras
cantidad_dolares = 100
cantidad_libras = convertir_moneda(cantidad_dolares, tasa_dolar_libra)
print(cantidad_dolares, "dólares son equivalentes a", cantidad_libras, "libras.")


# En este ejemplo, la función convertir_moneda toma la cantidad de dinero que se desea convertir y la tasa_conversion correspondiente a la tasa de cambio entre las dos monedas.
# Luego, se definen tasas de conversión para convertir dólares a euros y dólares a libras.
# A continuación, se utiliza la función convertir_moneda para convertir una cantidad de dólares a euros y libras, utilizando las tasas de conversión establecidas.

# Finalmente, se imprime el resultado de la conversión.