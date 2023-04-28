import os, sys
import json
sys.path.append('/Users/arnauadan/Desktop/TTM/sounds')
import download
import numpy as np
import matplotlib.pyplot as plt


########## EXERCISE 1 ##########

#download.download_sounds_freesound(queryText = "piano", tag=None, duration=10, API_Key = "9Afu6ii6lwYUfYrvCtYfPvVu8CxbWdFo02huS4Bz", outputDir = "/Users/arnauadan/Desktop/TTM/sounds/", topNResults = 5, featureExt = '.json')
#download.download_sounds_freesound(queryText = "violin", tag=None, duration=10, API_Key = "9Afu6ii6lwYUfYrvCtYfPvVu8CxbWdFo02huS4Bz", outputDir = "/Users/arnauadan/Desktop/TTM/sounds", topNResults = 5, featureExt = '.json')
#download.download_sounds_freesound(queryText = "cello", tag=None, duration=10, API_Key = "9Afu6ii6lwYUfYrvCtYfPvVu8CxbWdFo02huS4Bz", outputDir = "/Users/arnauadan/Desktop/TTM/sounds", topNResults = 5, featureExt = '.json')

"""""""""
########## EXPLANATION ##########
After run, we can see in the directory choosed on folder with the name of the instrument that we have put in the function. 
Inside of every folder we can find 5 different (as we mark with topNResults variable) folder with their id and an 
'.txt' file (with the index of the every 'id).
Finally inside every folder we see two different files: '.json' (with all the needed data of the descriptors) 
and another '.mp3' file (with the sound thtat with ).
If we play the audio clip, we can hear that not every sound is the instrument that we choosed, but could be some similar
descriptors.
"""""""""

########## EXERCISE 2 ##########
"""""""""
inputDir = "/Users/arnauadan/Desktop/TTM/sounds/"

descInput = (7, 10)

anotOn = 0
dataDetails = download.fetchDataDetails(inputDir)
colors = ['r', 'g', 'c', 'b', 'k', 'm', 'y']

plt.figure(figsize=(15, 10))

legArray = []
catArray = []
for ii, category in enumerate(dataDetails.keys()):
    catArray.append(category)
    for soundId in dataDetails[category].keys():
        filepath = os.path.join(inputDir, category, soundId, dataDetails[category][soundId]['file'])
        descSound = download.convFtrDict2List(json.load(open(filepath, 'r')))
        x_cord = descSound[descInput[0]]
        y_cord = descSound[descInput[1]]
        plt.scatter(x_cord, y_cord, c=colors[ii], s=200, alpha=0.75)
        if anotOn == 1:
            plt.annotate(soundId, xy=(x_cord, y_cord), xytext=(x_cord, y_cord))
    circ = plt.Line2D([0], [0], linestyle="none", marker="o", alpha=0.75, markersize=10, markerfacecolor=colors[ii])
    legArray.append(circ)

plt.ylabel(download.descriptorMapping[descInput[1]])
plt.xlabel(download.descriptorMapping[descInput[0]])
plt.legend(legArray, catArray, numpoints=1, bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=len(catArray), mode="expand", borderaxespad=0.)
plt.show()
"""""
"""""""""
########## EXPLANATION ##########
Following the code above we are classifying the different sounds over the descriptors. 
So, we can see the five sounds of every instrument downloaded ina graph classified in different means of descriptors. 
"""""""""

########## EXERCISE 3 ##########

#cluster = download.cluster_sounds(inputDir, nCluster=5, descInput=[10, 12])

"""""""""
########## EXPLANATION ##########
We see a print that assign different number depending on the proximity of the mean of the descriptors.
In our case as we run different time, the descriptors are closer and at least we at most get 60%.
"""""""""

########## EXERCISE 4.1 ##########

queryFile = '/Users/arnauadan/Desktop/TTM/sounds/cello/60055/60055_649468-lq.json'
targetDir = '/Users/arnauadan/Desktop/TTM/sounds/cello/60055'
queryText = download.compute_similar_sounds(queryFile, targetDir, descInput=[6, 12])
download.download_sounds_freesound(queryText=queryText[0][2], tag=None, duration=10, API_Key = "9Afu6ii6lwYUfYrvCtYfPvVu8CxbWdFo02huS4Bz", outputDir = "/Users/arnauadan/Desktop/TTM/sounds/", topNResults = 5, featureExt = '.json')

"""""""""
########## EXPLANATION ##########
Far from hearing that the 5 sounds are cello, more or less we feel that are a little similar, better than before.
"""""""""

########## EXERCISE 4.2 ##########



"""""""""
########## EXPLANATION ##########

"""""""""