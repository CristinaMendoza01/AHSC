import pandas as pd
import csv
# Supongamos que tienes nuevos sonidos en la matriz 'new_sounds'

# Leer el archivo CSV
def drop_id_col(data_file):
    new_data = pd.read_csv(data_file)

    copia = new_data.copy()

    columns_to_exclude = ['id']  # Reemplaza 'columna_96' y 'columna_97' con los nombres reales de tus columnas

# Elimina las columnas a excluir del DataFrame de nuevos sonidos
    new_copy = copia.drop(columns=columns_to_exclude)

    new_csv_file = 'horrorsounds-id.csv'  # Nombre del nuevo archivo CSV

# Guardar el DataFrame con las columnas eliminadas en un nuevo archivo CSV
    new_copy.to_csv(new_csv_file, index=False)

data_file = 'horrorSounds.csv'
#drop_id_col(data_file)
def del_low_accuracy(fulldata):
    df = pd.read_csv(fulldata)

    df_deleted = df[(df['clase'] != 'Alarm') & (df['clase'] != 'door_window')& (df['clase'] != 'RespiratorySounds') & (df['clase'] != 'explosion')]

    df_deleted.to_csv('clases_filtrados.csv', index=False)

fulldata = 'fulldata.csv'
del_low_accuracy(fulldata)