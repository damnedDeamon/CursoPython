# Importar el módulo datetime:
import datetime



# Obtener la fecha y hora actual:
fecha_actual = datetime.datetime.now()
print(fecha_actual)  # Imprime la fecha y hora actual



# Obtener la fecha actual:
fecha_actual = datetime.date.today()
print(fecha_actual)  # Imprime la fecha actual



# Crear una fecha específica:
fecha = datetime.date(2023, 7, 1)
print(fecha)  # Imprime la fecha: 2023-07-01



# Crear una hora específica:
hora = datetime.time(12, 30, 45)
print(hora)  # Imprime la hora: 12:30:45



# Trabajar con fechas y tiempos:
fecha_actual = datetime.date.today()
print(fecha_actual.year)  # Obtener el año actual
print(fecha_actual.month)  # Obtener el mes actual
print(fecha_actual.day)  # Obtener el día actual

hora_actual = datetime.datetime.now().time()
print(hora_actual.hour)  # Obtener la hora actual
print(hora_actual.minute)  # Obtener los minutos actuales
print(hora_actual.second)  # Obtener los segundos actuales



# Formatear una fecha y hora:
fecha_hora_actual = datetime.datetime.now()
fecha_hora_formateada = fecha_hora_actual.strftime("%d-%m-%Y %H:%M:%S")
print(fecha_hora_formateada)  # Imprime la fecha y hora formateada