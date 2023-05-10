import os
import shutil
import zipfile
import tarfile

# Ruta del archivo zip
#ruta_zip = "C:/Users/laiad/Documents/Universitat/TTM/Sounds/unsplit/union/fusion.zip"
ruta_zip = "C:/Users/laiad/Documents/Universitat/TTM/Sounds/FSD50K.dev_audio.zip"


# Carpeta donde se extraerán los archivos del zip
carpeta_temporal = "C:/Users/laiad/Desktop/temporal_folder"

# Palabras clave para buscar archivos
palabras_clave = ["754", "1262.wav", "1269.wav", "1271.wav", "2432.wav", "2434.wav", "4503.wav",
                  "8890.wav","10608.wav", "10609.wav", "10611.wav", "10612.wav", "10613.wav",
                  "10615.wav", "10618.wav", "10620.wav", "10623.wav", "10624.wav", "10625.wav", "10628.wav"]

# Directorio donde se moverán los archivos encontrados
nuevo_directorio = "C:/Users/laiad/Desktop/Class 1/"

# Extraer los archivos del zip en la carpeta temporal
with zipfile.ZipFile(ruta_zip, 'r', compression=zipfile.ZIP_DEFLATED) as zip_ref:
    zip_ref.extractall(carpeta_temporal)


# Buscar y mover los archivos en la carpeta temporal
for archivo in os.listdir(carpeta_temporal):
    if any(palabra_clave in archivo for palabra_clave in palabras_clave):
        shutil.move(os.path.join(carpeta_temporal, archivo), nuevo_directorio)
        print("Moved:", archivo)

# Eliminar la carpeta temporal
shutil.rmtree(carpeta_temporal)
