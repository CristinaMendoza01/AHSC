import json
import os
import freesound as fs

descriptors = [ 'lowlevel.spectral_centroid.mean',
                'lowlevel.spectral_contrast.mean',
                'lowlevel.dissonance.mean',
                'lowlevel.hfc.mean',
                'lowlevel.mfcc.mean',
                'sfx.logattacktime.mean',
                'sfx.inharmonicity.mean']

def download_sounds_freesound(query, directory, api_key, topNresults, featureExt='.json'):
    if query == "":
        print("\n")
        print("Provide a query text to search for sounds")
        return -1

    if api_key == "":
        print("\n")
        print("You need a valid freesound API key to be able to download sounds.")
        print("Please apply for one here: www.freesound.org/apiv2/apply/")
        print("\n")
        return -1

    if directory == "" or not os.path.exists(directory):
        print("\n")
        print(
            "Please provide a valid output directory. This will be the root directory for storing sounds and descriptors")
        return -1

    # Crea un cliente de Freesound y establece el token de API
    client = fs.FreesoundClient()
    client.set_token(api_key, "token")

    # Busca sonidos por el texto de búsqueda
    # Querying Freesound
    page_size = 30
    results = client.text_search(query=query, fields="id,name,previews", page_size=page_size)

    # Crea el directorio si aún no existe
    if not os.path.exists(directory):
        os.makedirs(directory)

    dir_path = os.path.join(directory, query)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    # Descarga y guarda cada sonido en el directorio
    for sound in results:
        sound.retrieve_preview(dir_path, sound.name)
        print(f"Saving {sound.name} in {dir_path}")

    mp3Path = os.path.join(directory, str(sound.previews.preview_lq_mp3.split("/")[-1]))
    print(mp3Path)
    ftrPath = mp3Path.replace('.mp3', featureExt)
    print(ftrPath)
    # Creating directories to store output and downloading sounds and their descriptors
    # pageNo = 1
    # sndCnt = 0
    # indCnt = 0
    # totalSnds = min(results.count, 200)  # System quits after trying to download after 200 times
    #
    # downloadedSounds = []
    # while (1):
    #     if indCnt >= totalSnds:
    #         print(
    #             "Not able to download required number of sounds. Either there are not enough search results on freesound for your search query and filtering constraints or something is wrong with this script.")
    #         break
    #     sound = results[indCnt - ((pageNo - 1) * page_size)]
    #     print("Downloading mp3 preview and descriptors for sound with id: %s" % str(sound.id))
    #     outDir1 = os.path.join(directory, query, str(sound.id))
    #
    #     mp3Path = os.path.join(outDir1, str(sound.previews.preview_lq_mp3.split("/")[-1]))
    #     ftrPath = mp3Path.replace('.mp3', featureExt)
    #
    #
    #     fs.FSRequest.retrieve(sound.previews.preview_lq_mp3, client, mp3Path)
    #     # Initialize a dictionary to store descriptors
    #     features = {}
    #     # Obtaining all the descriptors
    #     for desc in descriptors:
    #         features[desc] = []
    #         features[desc].append(eval("sound.analysis." + desc))
    #
    #     # Once we have all the descriptors, store them in a json file
    #     json.dump(features, open(ftrPath, 'w'))
    #     sndCnt += 1
    #     downloadedSounds.append([str(sound.id), sound.url])
    #
    #     indCnt += 1
    #
    #     if indCnt % page_size == 0:
    #         results = results.next_page()
    #         pageNo += 1
    #
    #     if sndCnt >= topNresults:
    #         break
    #
    #     # Dump the list of files and Freesound links
    #     fid = open(os.path.join(outDir2, query + '_SoundList.txt'), 'w')
    #     for elem in downloadedSounds:
    #         fid.write('\t'.join(elem) + '\n')
    #     fid.close()