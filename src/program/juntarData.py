import csv
import os
import pandas as pd

archivos_csv = ['Data/data.csv', 'Data/data1.csv', 'Data/data2.csv', 'Data/data3.csv', 'Data/data4.csv', 'Data/data5.csv']

dfs = []
for archivo in archivos_csv:
    df = pd.read_csv(archivo)
    dfs.append(df)

resultado = pd.concat(dfs, ignore_index=True)


resultado.to_csv('FullData.csv', index=False)
