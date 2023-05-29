import essentia
import os
import matplotlib.pyplot as plt
import numpy as np
import glob


# Imports to support MIR
import mirdata
import essentia.standard as ess
import pandas as pd




dataset_path = '/home/naiaragarmendia/Documents/GitHub/AHSC/src/program/trainingSet'  # Reemplaza con la ruta correcta a tu carpeta dataset

classes = []
mp3_files = glob.glob(dataset_path + '/**/*.mp3', recursive=True)  # Obtener la lista de archivos MP3


for i, mp3_file in enumerate(mp3_files):
    folder_path = os.path.dirname(mp3_file)  # Obtener la ruta de la carpeta
    audio_name = os.path.dirname(folder_path) # Obtener el nombre de la carpeta
    folder_name = os.path.basename(audio_name)
    if folder_name not in classes:
        classes.append(folder_name)  # Agregar la clase a la lista de clases


# Crear un diccionario utilizando el tipo de golpe como clave
stroke_dict = {item: [] for item in classes}
for i, mp3_file in enumerate(mp3_files):
    folder_path = os.path.dirname(mp3_file)  # Obtener la ruta de la carpeta
    folder_name = os.path.dirname(folder_path)
    folder_name = os.path.basename(folder_name)  # Obtener el nombre de la carpeta
    stroke_dict[folder_name].append(mp3_file)  # Agregar la data al diccionario

print(stroke_dict['bell'])
###########################################################################################################################

# Raw-data preprocess analysis parameters
windowSize = 1024
hopSize = 512
NRG_threshold_ratio = 0.005 #threshold expressed as ratio with respect to the maximum value
fs = 44100
#Let's put in a container to be able to use as a single argument in function calls
params = {"fs":fs, "windowSize":windowSize, "hopSize":hopSize, "NRG_threshold_ratio": NRG_threshold_ratio}
def split_file(filename, params):
    '''Function to define split boundaries based on a fixed energy threshold
    '''
    x = ess.MonoLoader(filename=filename, sampleRate=fs)()
    NRG = [];
    # Main windowing and feature extraction loop
    for frame in ess.FrameGenerator(x, frameSize=windowSize, hopSize=hopSize, startFromZero=True):
        NRG.append(ess.Energy()(frame))
    NRG = np.array(NRG)
    NRG = NRG / np.max(NRG)

    # Applying energy threshold to decide wave split boundaries
    split_decision_func = np.zeros_like(NRG)
    split_decision_func[NRG > NRG_threshold_ratio] = 1
    # Setting segment boundaries
    # Inserting a zero at the beginning since we will decide the transitions using a diff function
    split_decision_func = np.insert(split_decision_func, 0, 0)
    diff_split_decision = np.diff(split_decision_func)
    # Start indexes: transition from 0 to 1
    start_indexes = np.nonzero(diff_split_decision > 0)[0] * hopSize
    # Stop indexes: transition from 1 to 0
    stop_indexes = np.nonzero(diff_split_decision < 0)[0] * hopSize
    return (x, NRG, split_decision_func, start_indexes, stop_indexes)


###########################################################################################################3
main_data_dir = '/home/naiaragarmendia/Documents/GitHub/AHSC/src/program'
segments_dir = os.path.join(main_data_dir,'segments')
if not os.path.exists(segments_dir): #creating the directory
    os.mkdir(segments_dir)


segment_files = []
for stroke, files in stroke_dict.items():
    for sample_file in files:
        #Get file id
        stroke_id =  sample_file.split('__')[-1].split('.')[0]
        x = ess.MonoLoader(filename = sample_file, sampleRate = fs)()
        (x, NRG, split_decision_func, start_indexes, stop_indexes) = split_file(sample_file, params)
        #Croping segments
        for start, stop in zip(start_indexes, stop_indexes):
            x_seg = x[start: stop]
            #Final check for amplitude (to avoid silent segments selection due to noise in split function)
            if(np.max(np.abs(x_seg)) > 0.05):
                #Amplitude normalisation
                x_seg = x_seg / np.max(np.abs(x_seg))
                filename = os.path.join(segments_dir, stroke_id + '.wav')
                ess.MonoWriter(filename = filename, format = 'wav', sampleRate = fs)(x_seg)
                segment_files.append(filename)

print(len(segment_files),'segment files created')

############################################################################################################# hasta aqui crea los segmentos.

audio_path = mp3_files[1]
features, features_frames = ess.FreesoundExtractor(lowlevelSilentFrames='drop',
                                                      lowlevelFrameSize = 2048,
                                                      lowlevelHopSize = 1024,
                                                      lowlevelStats = ['mean', 'stdev'])(audio_path)

scalar_lowlevel_descriptors = [descriptor for descriptor in features.descriptorNames() if 'lowlevel' in descriptor and isinstance(features[descriptor], float)]
print("Subset of features to be considered:\n",scalar_lowlevel_descriptors)
print(len(scalar_lowlevel_descriptors))


############################################################################################################

# Extracting features and writing in data.csv file in the segments folder
#  each line in the data.csv file represents a sample with features and the class information as the last element
data_file = '/home/naiaragarmendia/Documents/GitHub/AHSC/src/program/data.csv'
file_count = 0
with open(data_file, 'w') as writer:
    #adding column names as the first line in csv
    line2write = ','.join(scalar_lowlevel_descriptors + ['stroke']).replace('lowlevel.','') + '\n'
    writer.write(line2write)
    for filename in segment_files:
        file_count +=1
        if file_count % 20 == 0: #print name of a file every 20 files
            print(file_count, "files processed, current file: ", filename)

        #Compute and write features for file
        features, features_frames = ess.FreesoundExtractor(lowlevelSilentFrames='drop',
                                                      lowlevelFrameSize = 2048,
                                                      lowlevelHopSize = 1024,
                                                      lowlevelStats = ['mean', 'stdev'])(filename)
        selected_features = [features[descriptor] for descriptor in scalar_lowlevel_descriptors]
        label = filename.split('/')[-1].split('.')[0].split('-')[0]
        line2write = str(selected_features)[1:-1] + ',' + label + '\n'
        writer.write(line2write)
print("A total of ", file_count, "files processed")