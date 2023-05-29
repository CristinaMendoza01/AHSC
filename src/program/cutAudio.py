import os
from pydub import AudioSegment
import glob


def recortar_audio(input_path, output_path, duracion):
    audio = AudioSegment.from_file(input_path)
    duracion_ms = duracion * 1000  # Convertir a milisegundos
    audio_recortado = audio[:duracion_ms]  # Recortar el audio

    audio_recortado.export(output_path, format='wav')  # Exportar el audio recortado como archivo mp3
    print("audio recortado")


# Carpeta que contiene los archivos de audio
carpeta_principal = '/home/naiaragarmendia/Desktop/Dataset'

# Duración deseada en segundos
duracion_deseada = 5

# Obtener la lista de archivos de audio en las subcarpetas
archivos_audio = glob.glob(os.path.join(carpeta_principal, '**', '*.wav'), recursive=True)

# Iterar sobre los archivos y recortarlos
for archivo in archivos_audio:
    nombre_archivo = os.path.basename(archivo)

    carpeta_salida = os.path.dirname(archivo)
    carpeta_salida_recortada = os.path.join(carpeta_salida, 'recortado')
    archivo_salida = os.path.join(carpeta_salida_recortada, nombre_archivo)

    os.makedirs(carpeta_salida_recortada, exist_ok=True)

    recortar_audio(archivo, archivo_salida, duracion_deseada)
