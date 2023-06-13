import pandas as pd
import csv
# Supongamos que tienes nuevos sonidos en la matriz 'new_sounds'
new_data_file = 'horrorSounds.csv'

# Leer el archivo CSV
new_data = pd.read_csv(new_data_file)

copia = new_data.copy()

columns_to_exclude = ['id']  # Reemplaza 'columna_96' y 'columna_97' con los nombres reales de tus columnas

# Elimina las columnas a excluir del DataFrame de nuevos sonidos
new_copy = copia.drop(columns=columns_to_exclude)

new_csv_file = 'horrorsounds-id.csv'  # Nombre del nuevo archivo CSV

# Guardar el DataFrame con las columnas eliminadas en un nuevo archivo CSV
new_copy.to_csv(new_csv_file, index=False)
