import essentia
import os
import matplotlib.pyplot as plt
import numpy as np
import glob


# Imports to support MIR
import mirdata
import essentia.standard as ess
import pandas as pd


def create_data_csv(input_dataset):
    classes = []
    audio_files = glob.glob(input_dataset + '/**/*.wav', recursive=True)

    for i, audio_file in enumerate(audio_files):
        folder_path = os.path.dirname(audio_file)  # Obtener la ruta de la carpeta
        folder_name = os.path.basename(folder_path) # Obtener el nombre de la carpeta
        if folder_name not in classes:
            classes.append(folder_name)

    print(classes)

    # Crear un diccionario utilizando el tipo de golpe como clave
    stroke_dict = {item: [] for item in classes}
    for i, audio_file in enumerate(audio_files):
        folder_path = os.path.dirname(audio_file)  # Obtener la ruta de la carpeta
        folder_name = os.path.basename(folder_path)
        stroke_dict[folder_name].append(audio_file)  # Agregar la data al diccionario

    print(stroke_dict)

    ############################################################################################################# hasta aqui crea los segmentos.
    #getting the names of the descriptors for FreesoundExtractor
    audio_path = audio_files[1]
    features, features_frames = ess.FreesoundExtractor(lowlevelSilentFrames='drop',
                                                          lowlevelFrameSize = 2048,
                                                          lowlevelHopSize = 1024,
                                                          lowlevelStats = ['mean', 'stdev'])(audio_path)

    scalar_lowlevel_descriptors = [descriptor for descriptor in features.descriptorNames() if 'lowlevel' in descriptor and isinstance(features[descriptor], float)]
    print("Subset of features to be considered:\n",scalar_lowlevel_descriptors)
    print(len(scalar_lowlevel_descriptors))


    ############################################################################################################



    data_file = '/home/naiaragarmendia/Documents/GitHub/AHSC/src/program/Data/data12.csv'
    file_count = 0

    with open(data_file, 'w') as writer:
        # Agregar nombres de columna como la primera línea en el archivo CSV
        line2write = ','.join(scalar_lowlevel_descriptors + ['clase']).replace('lowlevel.','')  + '\n'
        writer.write(line2write)

        for filename in audio_files:
            file_count += 1

            #if file_count % 20 == 0:  # Imprimir el nombre de un archivo cada 20 archivos
            print(file_count, "files processed, current file:", filename)

            # Obtener el nombre de la carpeta
            folder_name = os.path.basename(os.path.dirname(filename))

            try:
                # Calcular y escribir características para el archivo
                features, features_frames = ess.FreesoundExtractor(lowlevelSilentFrames='drop',
                                                                   lowlevelFrameSize=2048,
                                                                   lowlevelHopSize=1024,
                                                                   lowlevelStats=['mean', 'stdev'])(filename)

                selected_features = [features[descriptor] for descriptor in scalar_lowlevel_descriptors]
                line2write = str(selected_features)[1:-1] + ',' + folder_name + '\n'
                writer.write(line2write)

            except Exception as e:
                print(f"Error al procesar el archivo {filename}: {str(e)}")

                continue

    print("A total of", file_count, "files processed")
    return data_file

input_dataset = '/home/naiaragarmendia/Desktop/Dataset_recortado/Electronic Sounds Recortado/Alarm'


data = create_data_csv(input_dataset)