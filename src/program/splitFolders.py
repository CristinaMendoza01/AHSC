import os
import shutil

# Ruta de la carpeta principal
carpeta_principal = "C:/Users/laiad/Desktop/new classes/nightmare"

# Rutas de las carpetas para archivos .mp3 y .json
carpeta_mp3 = "C:/Users/laiad/Desktop/new classes/nightmare_mp3"
carpeta_json = "C:/Users/laiad/Desktop/new classes/nightmare_json"

# Crea las carpetas si no existen
if not os.path.exists(carpeta_mp3):
    os.makedirs(carpeta_mp3)

if not os.path.exists(carpeta_json):
    os.makedirs(carpeta_json)

# Recorre las subcarpetas y mueve los archivos
for root, dirs, files in os.walk(carpeta_principal):
    for archivo in files:
        ruta_archivo = os.path.join(root, archivo)
        if archivo.endswith(".mp3"):
            shutil.move(ruta_archivo, carpeta_mp3)
        elif archivo.endswith(".json"):
            shutil.move(ruta_archivo, carpeta_json)

print("Proceso completado.")
