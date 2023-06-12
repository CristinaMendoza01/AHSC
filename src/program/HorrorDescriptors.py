import essentia
import os
import matplotlib.pyplot as plt
import numpy as np
import glob


# Imports to support MIR
import mirdata
import essentia.standard as ess
import pandas as pd

def corpus_audios(input_dataset):
    audio_files = glob.glob(input_dataset + '/**/*.mp3', recursive=True)

    #############################################################################################################
    # Obteniendo los nombres de los descriptores para FreesoundExtractor
    audio_path = audio_files[1]
    features, features_frames = ess.FreesoundExtractor(lowlevelSilentFrames='drop',
                                                      lowlevelFrameSize=2048,
                                                      lowlevelHopSize=1024,
                                                      lowlevelStats=['mean', 'stdev'])(audio_path)

    scalar_lowlevel_descriptors = [descriptor for descriptor in features.descriptorNames() if 'lowlevel' in descriptor and isinstance(features[descriptor], float)]
    # print("Subset of features to be considered:\n",scalar_lowlevel_descriptors)
    # print(len(scalar_lowlevel_descriptors))

    ############################################################################################################

    data_file = '/home/naiaragarmendia/Documents/GitHub/AHSC/src/program/HorrorSounds/horrorsounds.csv'
    file_count = 0

    with open(data_file, 'w') as writer:
        # Agregar nombres de columna como la primera línea en el archivo CSV
        line2write = ','.join(scalar_lowlevel_descriptors).replace('lowlevel.', '') + ',id\n'
        writer.write(line2write)

        for filename in audio_files:
            file_count += 1

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

                # Obtener el ID del sonido del nombre del archivo
                sound_id = os.path.basename(filename).split('_')[0]

                line2write = str(selected_features)[1:-1] + ',' + folder_name + ',' + sound_id + '\n'
                writer.write(line2write)

            except Exception as e:
                print(f"Error al procesar el archivo {filename}: {str(e)}")
                continue

    print("A total of", file_count, "files processed")
    return data_file

input_dataset = '/home/naiaragarmendia/Desktop/horroSoundRecortado'

data = corpus_audios(input_dataset)