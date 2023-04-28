import sys
import functions as f

sys.path.append('./freesound-python-master/')  # directory were you installed the freesound-python repository

descriptors = [ 'lowlevel.spectral_centroid.mean',
                'lowlevel.spectral_contrast.mean',
                'lowlevel.dissonance.mean',
                'lowlevel.hfc.mean',
                'lowlevel.mfcc.mean',
                'sfx.logattacktime.mean',
                'sfx.inharmonicity.mean']

# Download the sounds
f.download_sounds_freesound(queryText="trumpet", tag="single_note", duration=5, API_Key="dCvdtqvTd7A4WhnDF3qSkTZafXKxVqQIxlCM85KR", outputDir="./testDownload", topNResults=5, featureExt=".json", descriptors=descriptors)
f.download_sounds_freesound(queryText="violin", tag="single_note", duration=5, API_Key="dCvdtqvTd7A4WhnDF3qSkTZafXKxVqQIxlCM85KR", outputDir="./testDownload", topNResults=5, featureExt=".json", descriptors=descriptors)
f.download_sounds_freesound(queryText="flute", tag="single_note", duration=5, API_Key="dCvdtqvTd7A4WhnDF3qSkTZafXKxVqQIxlCM85KR", outputDir="./testDownload", topNResults=5, featureExt=".json", descriptors=descriptors)

