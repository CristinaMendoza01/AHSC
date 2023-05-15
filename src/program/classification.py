import json
import numpy as np
import clustering as c
def compute_similar_sounds(queryFile, targetDir, descInput=[]):
    """
    This function returns similar sounds for a specific queryFile. Given a queryFile this function
    computes the distance of the query to all the sounds found in the targetDir and sorts them in
    the increasing order of the distance. This way we can obtain similar sounds to a query sound.

    Input:
      queryFile (string): Descriptor file (.json, unless changed)
      targetDir (string): Target directory to search for similar sounds (using their descriptor files)
      descInput (list) : list of indices of the descriptors to be used for similarity/distance computation
                         (see descriptorMapping)
    Output:
      List containing an ordered list of similar sounds.
    """

    dataDetails = c.fetchDataDetails(targetDir)

    # reading query feature dictionary
    qFtr = json.load(open(queryFile, 'r'))
    dist = []
    # Iterating over classes
    for cname in dataDetails.keys():
        # Iterating over sounds
        for sname in dataDetails[cname].keys():
            f1 = c.convFtrDict2List(qFtr)
            f2 = c.convFtrDict2List(dataDetails[cname][sname]['feature'])
            eucDist = np.sqrt(np.sum(np.power(np.array(f1[descInput]) - np.array(f2[descInput]), 2)))
            dist.append([eucDist, sname, cname])

    # Sorting the array based on the distance
    indSort = np.argsort(np.array(dist)[:, 0])
    return (np.array(dist)[indSort, :]).tolist()


def classify_sound_kNN(queryFile, targetDir, K, descInput=[]):
    """
    This function performs the KNN classification of a sound. The nearest neighbors are chosen from
    the sounds in the targetDir.

    Input:
      queryFile (string): Descriptor file (.json, unless changed)
      targetDir (string): Target directory to search for similar sounds (using their descriptor files)
      K (int) : Number of nearest neighbors to consider for KNN classification.
      descInput (list) : List of indices of the descriptors to be used for similarity/distance computation
                        (see descriptorMapping)
    Output:
      predClass (string): Predicted class of the query sound
    """
    distances = compute_similar_sounds(queryFile, targetDir, descInput)
    #print(distances)
    if len(np.where((np.array(distances)[:, 0].astype(np.float64)) == 0)[0]) > 0:
        print("Warning: We found an exact copy of the query file in the target directory. "
              "Beware of duplicates while doing KNN classification.")

    classes = (np.array(distances)[:K, 2]).tolist()
    freqCnt = []
    for ii in range(K):
        freqCnt.append(classes.count(classes[ii]))
    indMax = np.argmax(freqCnt)
    predClass = classes[indMax]
    print("This sample belongs to class: " + str(predClass))

    return predClass
