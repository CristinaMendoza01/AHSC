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
#d.download_sounds_freesound(query="scream", tag="human", duration=10, directory="trainingSet", api_key=apiCristina, topNresults=10, featureExt='.json')
#d.download_sounds_freesound(query="breathe", tag="human", duration=10, directory="trainingSet", api_key=apiCristina, topNresults=10, featureExt='.json')
#d.download_sounds_freesound(query="flute", tag="single-note", duration=10, directory="./src/program/testDownload", api_key=apiCristina, topNresults=15, featureExt='.json')

# Part 2
print("\nPart 2: Do clustering 1 \n")
c.clustering()

# Part 3
print("\nPart 3: Do clustering 2\n")
c.cluster_sounds("trainingSet", nCluster=-1, descInput=[0, 12])

# Part 4
#print("\nPart 4.1: Download the test sounds from Freesound \n")
#d.download_sounds_freesound(query="screaming", tag=None, duration=10, directory="testingSet", api_key=apiCristina, topNresults=1, featureExt='.json')
# d.download_sounds_freesound(query="piano", tag="single-note", duration=10, directory="./src/program/testClass", api_key=apiCristina, topNresults=15, featureExt='.json')