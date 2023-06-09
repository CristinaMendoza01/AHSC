import json
import os
import shutil

import freesound as fs

'''
descriptors = [ 'lowlevel.spectral_centroid.mean',
                'lowlevel.spectral_contrast.mean',
                'lowlevel.dissonance.mean',
                'lowlevel.hfc.mean',
                'lowlevel.mfcc.mean',
                'sfx.logattacktime.mean',
                'sfx.inharmonicity.mean']
'''

descriptors = ['average_loudness', 'barkbands_crest.mean', 'barkbands_crest.stdev', 'barkbands_flatness_db.mean', 'barkbands_flatness_db.stdev', 'barkbands_kurtosis.mean', 'barkbands_kurtosis.stdev', 'barkbands_skewness.mean', 'barkbands_skewness.stdev', 'barkbands_spread.mean', 'barkbands_spread.stdev', 'dissonance.mean', 'dissonance.stdev', 'dynamic_complexity', 'erbbands_crest.mean', 'erbbands_crest.stdev', 'erbbands_flatness_db.mean', 'erbbands_flatness_db.stdev', 'erbbands_kurtosis.mean', 'erbbands_kurtosis.stdev', 'erbbands_skewness.mean', 'erbbands_skewness.stdev', 'erbbands_spread.mean', 'erbbands_spread.stdev', 'hfc.mean', 'hfc.stdev', 'loudness_ebu128.integrated', 'loudness_ebu128.loudness_range', 'loudness_ebu128.momentary.mean', 'loudness_ebu128.momentary.stdev', 'loudness_ebu128.short_term.mean', 'loudness_ebu128.short_term.stdev', 'melbands_crest.mean', 'melbands_crest.stdev', 'melbands_flatness_db.mean', 'melbands_flatness_db.stdev', 'melbands_kurtosis.mean', 'melbands_kurtosis.stdev', 'melbands_skewness.mean', 'melbands_skewness.stdev', 'melbands_spread.mean', 'melbands_spread.stdev', 'pitch.mean', 'pitch.stdev', 'pitch_instantaneous_confidence.mean', 'pitch_instantaneous_confidence.stdev', 'pitch_salience.mean', 'pitch_salience.stdev', 'silence_rate_20dB.mean', 'silence_rate_20dB.stdev', 'silence_rate_30dB.mean', 'silence_rate_30dB.stdev', 'silence_rate_60dB.mean', 'silence_rate_60dB.stdev', 'silence_rate_90dB.mean', 'silence_rate_90dB.stdev', 'sound_start_frame', 'sound_stop_frame', 'spectral_centroid.mean', 'spectral_centroid.stdev', 'spectral_complexity.mean', 'spectral_complexity.stdev', 'spectral_crest.mean', 'spectral_crest.stdev', 'spectral_decrease.mean', 'spectral_decrease.stdev', 'spectral_energy.mean', 'spectral_energy.stdev', 'spectral_energyband_high.mean', 'spectral_energyband_high.stdev', 'spectral_energyband_low.mean', 'spectral_energyband_low.stdev', 'spectral_energyband_middle_high.mean', 'spectral_energyband_middle_high.stdev', 'spectral_energyband_middle_low.mean', 'spectral_energyband_middle_low.stdev', 'spectral_entropy.mean', 'spectral_entropy.stdev', 'spectral_flatness_db.mean', 'spectral_flatness_db.stdev', 'spectral_flux.mean', 'spectral_flux.stdev', 'spectral_kurtosis.mean', 'spectral_kurtosis.stdev', 'spectral_rms.mean', 'spectral_rms.stdev', 'spectral_rolloff.mean', 'spectral_rolloff.stdev', 'spectral_skewness.mean', 'spectral_skewness.stdev', 'spectral_spread.mean', 'spectral_spread.stdev', 'spectral_strongpeak.mean', 'spectral_strongpeak.stdev', 'zerocrossingrate.mean', 'zerocrossingrate.stdev']

def download_sounds_freesound(query, tag, duration, directory, api_key, topNresults, featureExt='.json'):
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

    # Creating a duration filter string that the Freesound API understands
    if duration and type(duration) == tuple:
        flt_dur = " duration:[" + str(duration[0]) + " TO " + str(duration[1]) + "]"
    else:
        flt_dur = ""

    if tag and type(tag) == str:
        flt_tag = "tag:" + tag
    else:
        flt_tag = ""

    # Busca sonidos por el texto de búsqueda
    # Querying Freesound
    page_size = 30
    if not flt_tag + flt_dur == "":
        results = client.text_search(query=query, filter=flt_tag + flt_dur, sort="score",
                                  fields="id,name,previews,username,url,analysis", descriptors=','.join(descriptors),
                                  page_size=page_size, normalized=1)

    else:
        results = client.text_search(query=query, sort="score", fields="id,name,previews,username,url,analysis",
                                  descriptors=','.join(descriptors), page_size=page_size, normalized=1)

    # Crea el directorio si aún no existe
    if not os.path.exists(directory):
        os.makedirs(directory)

    dir_path = os.path.join(directory + '/' + query)
    if os.path.exists(dir_path):
        print(dir_path)
        print(os.listdir(dir_path))
        shutil.rmtree(dir_path)
    os.mkdir(dir_path)

    pageNo = 1
    sndCnt = 0
    indCnt = 0
    totalSnds = results.count
    downloadedSounds = []

    if(not bool(os.listdir(dir_path))):

        #print(os.listdir(dir_path))

        # Creating directories to store output and downloading sounds and their descriptors
        while (1):
            if indCnt >= totalSnds:
                print(f"required number of sounds. {results.count}")
                break
            sound = results[indCnt - ((pageNo - 1) * page_size)]

            outDir = os.path.join(dir_path + '/' + str(sound.id))
            os.mkdir(outDir)

            print(f"{indCnt} Downloading mp3 preview and descriptors for sound with id: {sound.id}")

            mp3Path = os.path.join(outDir + '/' + str(sound.previews.preview_lq_mp3.split("/")[-1]))
            #print(mp3Path)
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

            except FileExistsError:
                print("We had a file exist error but try to continue..")
                continue
            except Exception as e:
                print(f"Error: {e}")

            indCnt += 1

            if indCnt % page_size == 0:
                results = results.next_page()
                pageNo += 1

            if sndCnt >= topNresults:
                break

        # Dump the list of files and Freesound links
        fid = open(os.path.join(dir_path, query + '_SoundList.txt'), 'w')
        for elem in downloadedSounds:
            fid.write('\t'.join(elem) + '\n')
        fid.close()
    else:
        print("Not empty")


if __name__ == "__main__":
    apiCristina = "dCvdtqvTd7A4WhnDF3qSkTZafXKxVqQIxlCM85KR"

    download_sounds_freesound(
        query="nightmare",
        tag=None,
        duration=10,
        directory="C:/Users/laiad/Desktop/new classes",
        api_key=apiCristina,
        topNresults=1320,
        featureExt='.json'
    )