import csv
import os
import pandas as pd
import glob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def juntar_archivos(DataPath):
    archivos_csv = glob.glob(DataPath + '/**/*.csv', recursive=True)

    dfs = []
    for archivo in archivos_csv:
        df = pd.read_csv(archivo)
        dfs.append(df)

    resultado = pd.concat(dfs, ignore_index=True)


    resultado.to_csv('fulldata.csv', index=False)


DataPath = '/home/naiaragarmendia/Documents/GitHub/AHSC/src/program/Data'
juntar_archivos(DataPath)


def plot_data(dataPath): ##Me da error
    # Carga el archivo CSV en un DataFrame
    data = pd.read_csv(dataPath)
    # Seleccionar un subconjunto aleatorio de los datos (por ejemplo, 1000 filas)
    subset_data = data.sample(n=1000, random_state=42)

    # Seleccionar las columnas numéricas para el gráfico
    numeric_columns = subset_data.select_dtypes(include=['float64', 'int64'])

    # Plotear el gráfico de dispersión de todas las variables
    sns.pairplot(numeric_columns, hue='clase')

    plt.show()

#dataPath = '/home/naiaragarmendia/Documents/GitHub/AHSC/src/program/Data/data.csv'
#plot_data(dataPath)
