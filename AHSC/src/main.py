import os
import sys

import download as d
import clustering as c
import classification as cl

sys.path.append('./freesound-python-master/')

apiCristina = "dCvdtqvTd7A4WhnDF3qSkTZafXKxVqQIxlCM85KR"

print(os.getcwd())

# Part 1
#d.download_sounds_freesound(query="trumpet", tag="single-note", duration=10, directory="./src/testDownload", api_key=apiCristina, topNresults=15, featureExt='.json')
#d.download_sounds_freesound(query="violin", tag="single-note", duration=10, directory="./src/testDownload", api_key=apiCristina, topNresults=15, featureExt='.json')
#d.download_sounds_freesound(query="flute", tag="single-note", duration=10, directory="./src/testDownload", api_key=apiCristina, topNresults=15, featureExt='.json')

# Part 2
#c.clustering() # No funciona

# Part 3
# c.cluster_sounds("./src/testDownload", nCluster=-1, descInput=[0, 12])

# Part 4
#d.download_sounds_freesound(query="guitar", tag="single-note", duration=10, directory="./src/testClass", api_key=apiCristina, topNresults=15, featureExt='.json')
#d.download_sounds_freesound(query="piano", tag="single-note", duration=10, directory="./src/testClass", api_key=apiCristina, topNresults=15, featureExt='.json')

# Funciona la función pero en vez de decir una clase (flute, violin o trumpet), da el nombre de la carpeta
cl.classify_sound_kNN("./src/testClass/guitar/91199/91199_1075352-lq.json", "./src/testDownload/", 5, descInput=[1, 12])
cl.classify_sound_kNN("./src/testClass/guitar/110455/110455_1075352-lq.json", "./src/testDownload/", 3, descInput=[2, 10])
cl.classify_sound_kNN("./src/testClass/piano/673720/673720_8981843-lq.json", "./src/testDownload/", 3, descInput = [0, 1, 14, 15])
