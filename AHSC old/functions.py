import json
import os
import freesound as fs
import numpy as np
from scipy.cluster.vq import whiten, kmeans
def download_sounds_freesound(queryText="", tag=None, duration=None, API_Key="", outputDir="", topNResults=5, featureExt='.json',
                              descriptors=None):
    """
    This function downloads sounds and their descriptors from freesound using the queryText and the
    tag specified in the input. Additionally, you can also specify the duration range to filter sounds
    based on duration.

    Inputs:
          (Input parameters marked with a * are optional)
          queryText (string): query text for the sounds (eg. "violin", "trumpet", "cello", "bassoon" etc.)
          tag* (string): tag to be used for filtering the searched sounds. (eg. "multisample",
                         "single-note" etc.)
          duration* (tuple): min and the max duration (seconds) of the sound to filter, eg. (0.2,15)
          API_Key (string): your api key, which you can obtain from : www.freesound.org/apiv2/apply/
          outputDir (string): path to the directory where you want to store the sounds and their
                              descriptors
          topNResults (integer): number of results(sounds) that you want to download
          featureExt (string): file extension for storing sound descriptors
    output:
          This function downloads sounds and descriptors, and then stores them in outputDir. In
          outputDir it creates a directory of the same name as that of the queryText. In this
          directory outputDir/queryText it creates a directory for every sound with the name
          of the directory as the sound id. Additionally, this function also dumps a text file
          containing sound-ids and freesound links for all the downloaded sounds in the outputDir.
          NOTE: If the directory outputDir/queryText exists, it deletes the existing contents
          and stores only the sounds from the current query.
    """

    # Checking for the compulsory input parameters
    if descriptors is None:
        descriptors = []
    if queryText == "":
        print("\n")
        print("Provide a query text to search for sounds")
        return -1

    if API_Key == "":
        print("\n")
        print("You need a valid freesound API key to be able to download sounds.")
        print("Please apply for one here: www.freesound.org/apiv2/apply/")
        print("\n")
        return -1

    if outputDir == "" or not os.path.exists(outputDir):
        print("\n")
        print("Please provide a valid output directory. This will be the root directory for storing sounds and descriptors")
        return -1

    # Setting up the Freesound client and the authentication key
    client = fs.FreesoundClient()
    client.set_token(API_Key, "token")

    # Creating a duration filter string that the Freesound API understands
    if duration and type(duration) == tuple:
        flt_dur = " duration:[" + str(duration[0]) + " TO " + str(duration[1]) + "]"
    else:
        flt_dur = ""

    if tag and type(tag) == str:
        flt_tag = "tag:" + tag
    else:
        flt_tag = ""

    # Querying Freesound
    page_size = 30
    if not flt_tag + flt_dur == "":
        qRes = client.text_search(query=queryText, filter=flt_tag + flt_dur, sort="score", fields="id,name,previews,username,url,analysis", descriptors=','.join(descriptors), page_size=page_size, normalized=1)

    else:
        qRes = client.text_search(query=queryText, sort="score", fields="id,name,previews,username,url,analysis",
                                  descriptors=','.join(descriptors), page_size=page_size, normalized=1)

    outDir2 = os.path.join(outputDir, queryText)
    if os.path.exists(outDir2):  # If the directory exists, it deletes it and starts fresh
        os.system("rm -r " + outDir2)
    os.mkdir(outDir2)

    pageNo = 1
    sndCnt = 0
    indCnt = 0
    totalSnds = min(qRes.count, 200)  # System quits after trying to download after 200 times

    # Creating directories to store output and downloading sounds and their descriptors
    downloadedSounds = []
    while (1):
        if indCnt >= totalSnds:
            print("Not able to download required number of sounds. Either there are not enough search results on freesound for your search query and filtering constraints or something is wrong with this script.")
            break
        sound = qRes[indCnt - ((pageNo - 1) * page_size)]
        print("Downloading mp3 preview and descriptors for sound with id: %s" % str(sound.id))
        outDir1 = os.path.join(outputDir, queryText, str(sound.id))
        if os.path.exists(outDir1):
            os.system("rm -r " + outDir1)
        os.system("mkdir " + outDir1)

        mp3Path = os.path.join(outDir1, str(sound.previews.preview_lq_mp3.split("/")[-1]))
        ftrPath = mp3Path.replace('.mp3', featureExt)

        try:
            fs.FSRequest.retrieve(sound.previews.preview_lq_mp3, client, mp3Path)
            # Initialize a dictionary to store descriptors
            features = {}
            # Obtaining all the descriptors
            for desc in descriptors:
                features[desc] = []
                features[desc].append(eval("sound.analysis." + desc))

            # Once we have all the descriptors, store them in a json file
            json.dump(features, open(ftrPath, 'w'))
            sndCnt += 1
            downloadedSounds.append([str(sound.id), sound.url])

        except:
            if os.path.exists(outDir1):
                os.system("rm -r " + outDir1)

        indCnt += 1

        if indCnt % page_size == 0:
            qRes = qRes.next_page()
            pageNo += 1

        if sndCnt >= topNResults:
            break

    # Dump the list of files and Freesound links
    fid = open(os.path.join(outDir2, queryText +'_SoundList.txt'), 'w')
    for elem in downloadedSounds:
        fid.write('\t'.join(elem) + '\n')
    fid.close()

def convFtrDict2List(ftrDict, descriptorMapping):
    """
    This function converts descriptor dictionary to an np.array. The order in the numpy array (indices)
    are same as those mentioned in descriptorMapping dictionary.

    Input:
      ftrDict (dict): dictionary containing descriptors downloaded from the freesound
    Output:
      ftr (np.ndarray): Numpy array containing the descriptors for processing later on
    """
    ftr = []
    for key in range(len(descriptorMapping.keys())):
        try:
            ftrName, ind = '.'.join(descriptorMapping[key].split('.')[:-1]), int(descriptorMapping[key].split('.')[-1])
            ftr.append(ftrDict[ftrName][0][ind])
        except:
            ftr.append(ftrDict[descriptorMapping[key]][0])
    return np.array(ftr)


def fetchDataDetails(inputDir, descExt='.json'):
    """
    This function is used by other functions to obtain the information regarding the directory structure
    and the location of descriptor files for each sound
    """
    dataDetails = {}
    for path, dname, fnames in os.walk(inputDir):
        for fname in fnames:
            if descExt in fname.lower():
                remain, rname, cname, sname = path.split('/')[:-3], path.split('/')[-3], path.split('/')[-2], \
                    path.split('/')[-1]
                if cname not in dataDetails:
                    dataDetails[cname] = {}
                fDict = json.load(open(os.path.join('/'.join(remain), rname, cname, sname, fname), 'r'))
                dataDetails[cname][sname] = {'file': fname, 'feature': fDict}
    return dataDetails

def cluster_sounds(targetDir, nCluster=-1, descInput=[]):
    """
    This function clusters all the sounds in targetDir using kmeans clustering.

    Input:
      targetDir (string): Directory where sound descriptors are stored (all the sounds in this
                          directory will be used for clustering)
      nCluster (int): Number of clusters to be used for kmeans clustering.
      descInput (list) : List of indices of the descriptors to be used for similarity/distance
                         computation (see descriptorMapping)
    Output:
      Prints the class of each cluster (computed by a majority vote), number of sounds in each
      cluster and information (sound-id, sound-class and classification decision) of the sounds
      in each cluster. Optionally, you can uncomment the return statement to return the same data.
    """

    dataDetails = fetchDataDetails(targetDir)

    ftrArr = []
    infoArr = []

    if nCluster == -1:
        nCluster = len(dataDetails.keys())
    for cname in dataDetails.keys():
        # iterating over sounds
        for sname in dataDetails[cname].keys():
            ftrArr.append(convFtrDict2List(dataDetails[cname][sname]['feature'])[descInput])
            infoArr.append([sname, cname])

    ftrArr = np.array(ftrArr)
    infoArr = np.array(infoArr)

    ftrArrWhite = whiten(ftrArr)
    centroids, distortion = kmeans(ftrArrWhite, nCluster)
    clusResults = -1 * np.ones(ftrArrWhite.shape[0])

    for ii in range(ftrArrWhite.shape[0]):
        diff = centroids - ftrArrWhite[ii, :]
        diff = np.sum(np.power(diff, 2), axis=1)
        indMin = np.argmin(diff)
        clusResults[ii] = indMin

    ClusterOut = []
    classCluster = []
    globalDecisions = []
    for ii in range(nCluster):
        ind = np.where(clusResults == ii)[0]
        freqCnt = []
        for elem in infoArr[ind, 1]:
            freqCnt.append(infoArr[ind, 1].tolist().count(elem))
        indMax = np.argmax(freqCnt)
        classCluster.append(infoArr[ind, 1][indMax])


        print("\n(Cluster: " + str(ii) + ") Using majority voting as a criterion this cluster belongs to " +
              "class: " + classCluster[-1])
        print("Number of sounds in this cluster are: " + str(len(ind)))
        decisions = []
        for jj in ind:
            if infoArr[jj, 1] == classCluster[-1]:
                decisions.append(1)
            else:
                decisions.append(0)
        globalDecisions.extend(decisions)
        print("sound-id, sound-class, classification decision")
        ClusterOut.append(np.hstack((infoArr[ind], np.array([decisions]).T)))
        print(ClusterOut[-1])
    globalDecisions = np.array(globalDecisions)
    totalSounds = len(globalDecisions)
    nIncorrectClassified = len(np.where(globalDecisions == 0)[0])
    print("Out of %d sounds, %d sounds are incorrectly classified considering that one cluster should "
          "ideally contain sounds from only a single class" % (totalSounds, nIncorrectClassified))
    print("You obtain a classification (based on obtained clusters and majority voting) accuracy "
          "of %.2f percentage" % round(float(100.0 * float(totalSounds - nIncorrectClassified) / totalSounds), 2))
    # return ClusterOut

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

    dataDetails = fetchDataDetails(targetDir)

    # reading query feature dictionary
    qFtr = json.load(open(queryFile, 'r'))
    dist = []
    # Iterating over classes
    for cname in dataDetails.keys():
        # Iterating over sounds
        for sname in dataDetails[cname].keys():
            f1 = convFtrDict2List(qFtr)
            f2 = convFtrDict2List(dataDetails[cname][sname]['feature'])
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