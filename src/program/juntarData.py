import csv
import os
import pandas as pd

archivos_csv = ['data.csv', 'data1.csv', 'data2.csv']

dfs = []
for archivo in archivos_csv:
    df = pd.read_csv(archivo)
    dfs.append(df)

resultado = pd.concat(dfs, ignore_index=True)

resultado.to_csv('FullData.csv', index=False)
