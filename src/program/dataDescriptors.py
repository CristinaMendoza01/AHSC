
import os
import glob
import essentia.standard as ess
import random

def create_data_csv(input_dataset):
    classes = []
    for i, audio_file in enumerate(audio_files):
        folder_path = os.path.dirname(audio_file)  # Obtener la ruta de la carpeta
        folder_name = os.path.basename(folder_path) # Obtener el nombre de la carpeta
        if folder_name not in classes:
            classes.append(folder_name)



    # Crear un diccionario utilizando el tipo de golpe como clave
    stroke_dict = {item: [] for item in classes}
    for i, audio_file in enumerate(audio_files):
        folder_path = os.path.dirname(audio_file)  # Obtener la ruta de la carpeta
        folder_name = os.path.basename(folder_path)
        stroke_dict[folder_name].append(audio_file)  # Agregar la data al diccionario

    print(stroke_dict)

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

    data_file = '/home/naiaragarmendia/Documents/GitHub/AHSC/src/program/Data/data+id.csv'
    file_count = 0

    with open(data_file, 'w') as writer:
        # Agregar nombres de columna como la primera línea en el archivo CSV
        line2write = ','.join(scalar_lowlevel_descriptors + ['clase', 'stroke', 'id']).replace('lowlevel.', '')  + '\n'
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
                sound_id = os.path.splitext(os.path.basename(filename))[0]

                line2write = str(selected_features)[1:-1] + ',' + folder_name + ',' + sound_id + '\n'
                writer.write(line2write)

            except Exception as e:
                print(f"Error al procesar el archivo {filename}: {str(e)}")
                continue

    print("A total of", file_count, "files processed")
    return data_file

def seleccionar_audios(input_dataset, cantidad_maxima):

    audio_files = glob.glob(input_dataset + '/**/*.wav', recursive=True)
    class_audios = {}
    classes =[]
    for i, audio_file in enumerate(audio_files):
        folder_path = os.path.dirname(audio_file)  # Obtener la ruta de la carpeta
        folder_name = os.path.basename(folder_path)  # Obtener el nombre de la carpeta
        if folder_name not in classes:
            classes.append(folder_name)
            class_audios[folder_name] = []  # Crear una lista vacía para almacenar los audios de cada clase

        class_audios[folder_name].append(audio_file)  # Agregar el archivo de audio a la lista correspondiente a su clase

    selected_audios = {}

    for clase, audios in class_audios.items():
        if len(audios) > cantidad_maxima:
            selected_audios[clase] = random.sample(audios, cantidad_maxima)  # Seleccionar aleatoriamente 480 audios de la clase
        else:
            selected_audios[clase] = audios

    audio_files = []

    for clase, audios in selected_audios.items():
        audio_files.extend(audios)

    return audio_files




input_dataset = '/home/naiaragarmendia/Desktop/Dataset_recortado'
audio_files = seleccionar_audios(input_dataset, 480)
create_data_csv(audio_files)



