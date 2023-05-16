import os
import sys

import download as d
import clustering as c
import classification as cl
import matplotlib as plt

sys.path.append('./freesound-python-master/')

apiCristina = "dCvdtqvTd7A4WhnDF3qSkTZafXKxVqQIxlCM85KR"

# print(os.getcwd())

# testClass --> testingSet
# testDownload --> trainingSet

# Part 1
#print("Part 1: Download the training sounds from Freesound\n")

######################### CRISTINA SOUNDS ##################################
#d.download_sounds_freesound(query="scream", tag="human", duration=10, directory="trainingSet", api_key=apiCristina, topNresults=10, featureExt='.json')
#d.download_sounds_freesound(query="breathe", tag="human", duration=10, directory="trainingSet", api_key=apiCristina, topNresults=10, featureExt='.json')
########################### SARA SOUNDS ####################################

########################## NAIARA SOUNDS ###################################

########################### ARNAU SOUNDS ###################################

########################### LAIA SOUNDS ####################################
#d.download_sounds_freesound(query="bowed string instrument", tag=None, duration=10, directory="trainingSet", api_key=apiCristina, topNresults=20, featureExt='.json')
#d.download_sounds_freesound(query="violin", tag='bowed', duration=10, directory="trainingSet", api_key=apiCristina, topNresults=20, featureExt='.json')
#d.download_sounds_freesound(query="viola", tag=None, duration=10, directory="trainingSet", api_key=apiCristina, topNresults=10, featureExt='.json')
#d.download_sounds_freesound(query="bell", tag=None, duration=10, directory="trainingSet", api_key=apiCristina, topNresults=50, featureExt='.json')
#d.download_sounds_freesound(query="guitar", tag="distorted", duration=10, directory="trainingSet", api_key=apiCristina, topNresults=50, featureExt='.json')
#d.download_sounds_freesound(query="guitar", tag=None, duration=5, directory="trainingSet", api_key=apiCristina, topNresults=30, featureExt='.json')
#d.download_sounds_freesound(query="piano", tag=None, duration=5, directory="trainingSet", api_key=apiCristina, topNresults=30, featureExt='.json')
########################## VÍCTOR SOUNDS ###################################
#d.download_sounds_freesound(query="door knocks", tag=None, duration=3, directory="trainingSet", api_key=apiCristina, topNresults=20, featureExt='.json')
############################################################################

#d.download_sounds_freesound(query="flute", tag="single-note", duration=10, directory="./src/program/testDownload", api_key=apiCristina, topNresults=15, featureExt='.json')

# Part 2
print("\nPart 2: Do clustering 1 \n")
#c.clustering()

# Part 3
print("\nPart 3: Do clustering 2\n")
#c.cluster_sounds("trainingSet", nCluster=-1, descInput=[0, 12])

# Part 4
#print("\nPart 4.1: Download the test sounds from Freesound \n")

############################## TESTING SOUNDS ######################################
######################### CRISTINA #################################
#d.download_sounds_freesound(query="screaming", tag="human", duration=10, directory="testingSet", api_key=apiCristina, topNresults=10, featureExt='.json')
########################### SARA ###################################
#d.download_sounds_freesound(query="car engine", tag=None, duration=30, directory="testingSet", api_key=apiCristina, topNresults=10, featureExt='.json')
########################## NAIARA ##################################
#d.download_sounds_freesound(query="rain", tag=None, duration=120, directory="testingSet", api_key=apiCristina, topNresults=10, featureExt='.json')
########################### ARNAU ##################################
#d.download_sounds_freesound(query="raven bird", tag=None, duration=530, directory="testingSet", api_key=apiCristina, topNresults=10, featureExt='.json')
########################### LAIA ###################################
#d.download_sounds_freesound(query="violin", tag=None, duration=50, directory="testingSet", api_key=apiCristina, topNresults=10, featureExt='.json')
########################## VÍCTOR ##################################
#d.download_sounds_freesound(query="knocking", tag="knock", duration=10, directory="testingSet", api_key=apiCristina, topNresults=10, featureExt='.json')
#####################################################################################


############################### CORPUS SOUNDS #######################################
d.download_sounds_freesound(query="horror sounds", tag=None, duration=10, directory="testingSet", api_key=apiCristina, topNresults=20, featureExt='.json')
#####################################################################################


#d.download_sounds_freesound(query="screaming", tag=None, duration=10, directory="testingSet", api_key=apiCristina, topNresults=1, featureExt='.json')
# d.download_sounds_freesound(query="piano", tag="single-note", duration=10, directory="./src/program/testClass", api_key=apiCristina, topNresults=15, featureExt='.json')