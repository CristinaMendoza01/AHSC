import os
import sys

import download as d
import clustering as c
import classification as cl
import matplotlib as plt



sys.path.append('./freesound-python-master/')

apiCristina = "dCvdtqvTd7A4WhnDF3qSkTZafXKxVqQIxlCM85KR"


# print(os.getcwd())

# Part 1
# print("Part 1: \n")
d.download_sounds_freesound(query="rain", tag="", duration=15, directory="testDownload", api_key=apiCristina, topNresults=50, featureExt='.json')
# d.download_sounds_freesound(query="violin", tag="single-note", duration=10, directory="./src/notebook/testDownload", api_key=apiCristina, topNresults=15, featureExt='.json')
# d.download_sounds_freesound(query="flute", tag="single-note", duration=10, directory="./src/notebook/testDownload", api_key=apiCristina, topNresults=15, featureExt='.json')

# Part 2
# print("\nPart 2: \n")
#c.clustering()


# Part 3
# print("\nPart 3: \n")
#c.cluster_sounds("testDownload", nCluster=-1, descInput=[0, 12])

# Part 4
# print("\nPart 4.1: \n")
# d.download_sounds_freesound(query="guitar", tag="single-note", duration=10, directory="./src/notebook/testClass", api_key=apiCristina, topNresults=15, featureExt='.json')
# d.download_sounds_freesound(query="piano", tag="single-note", duration=10, directory="./src/notebook/testClass", api_key=apiCristina, topNresults=15, featureExt='.json')

# Funciona la función pero en vez de decir una clase (flute, violin o trumpet), da el nombre de la carpeta
#print("\nPart 4.2: \n")
#cl.classify_sound_kNN("./src/notebook/testClass/guitar/91199/91199_1075352-lq.json", "./src/notebook/testDownload/", 5, descInput=[1, 12])
#cl.classify_sound_kNN("testClass/guitar/399479/399479_7575123-lq.json", "testDownload",5, descInput=[2,10])
#cl.classify_sound_kNN("./src/notebook/testClass/guitar/110455/110455_1075352-lq.json", "./src/notebook/testDownload/", 3, descInput=[2, 10])
#c
# l.classify_sound_kNN("./src/notebook/testClass/piano/673720/673720_8981843-lq.json", "./src/notebook/testDownload/", 3, descInput = [0, 1, 14, 15])

# Download Voice Sounds
#d.download_sounds_freesound(query="scream", tag=None, duration=None, directory="C:/Users/cris/downloads/voices", api_key=apiCristina, topNresults=500, featureExt='.json')

#d.download_sounds_freesound(query="whisper", tag=None, duration=None, directory="C:/Users/cris/downloads/voices", api_key=apiCristina, topNresults=500, featureExt='.json')

#d.download_sounds_freesound(query="monster", tag=None, duration=None, directory="C:/Users/cris/downloads/voices", api_key=apiCristina, topNresults=500, featureExt='.json')
#d.download_sounds_freesound(query="ghost", tag=None, duration=None, directory="C:/Users/cris/downloads/voices", api_key=apiCristina, topNresults=500, featureExt='.json')

#d.download_sounds_freesound(query="breathe", tag=None, duration=None, directory="C:/Users/cris/downloads/voices", api_key=apiCristina, topNresults=500, featureExt='.json')
# d.download_sounds_freesound(query="breathing", tag=None, duration=None, directory="C:/Users/cris/downloads/voices", api_key=apiCristina, topNresults=500, featureExt='.json')

#d.download_sounds_freesound(query="laugh", tag=None, duration=None, directory="C:/Users/cris/downloads/voices", api_key=apiCristina, topNresults=500, featureExt='.json')
#d.download_sounds_freesound(query="laughter", tag=None, duration=None, directory="C:/Users/cris/downloads/voices", api_key=apiCristina, topNresults=500, featureExt='.json')