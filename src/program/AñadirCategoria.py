import csv
import os

# Lectura del archivo CSV existente
with open('data.csv', 'r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    datos = list(lector_csv)

# Crear una lista de nombres de carpeta únicos
categorias = []
for fila in datos:
    nombre_archivo = fila[datos[0].index('stroke')]  # Busca el índice de la columna 'stroke'
    carpeta = os.path.dirname(nombre_archivo)
    if carpeta not in categorias:
        categorias.append(carpeta)

# Añadir la nueva columna "categoria" con los valores correspondientes
datos[0].append('categoria')  # Añade el encabezado de la columna
for fila in datos[1:]:  # Ignora la primera fila (encabezados de las columnas)
    nombre_archivo = fila[datos[0].index('stroke')]
    carpeta = os.path.dirname(nombre_archivo)
    fila.append(carpeta)

# Escribir los datos actualizados en un nuevo archivo CSV
with open('datos_actualizados.csv', 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerows(datos)
