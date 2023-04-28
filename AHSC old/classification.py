import functions as f

descriptors = [ 'lowlevel.spectral_centroid.mean',
                'lowlevel.spectral_contrast.mean',
                'lowlevel.dissonance.mean',
                'lowlevel.hfc.mean',
                'lowlevel.mfcc.mean',
                'sfx.logattacktime.mean',
                'sfx.inharmonicity.mean']

# Part 4
# 4.1
f.download_sounds_freesound(queryText="guitar", tag="single_note", duration=5, API_Key="dCvdtqvTd7A4WhnDF3qSkTZafXKxVqQIxlCM85KR", outputDir="./testClass", topNResults=5, featureExt=".json", descriptors=descriptors)
f.download_sounds_freesound(queryText="piano", tag="single_note", duration=5, API_Key="dCvdtqvTd7A4WhnDF3qSkTZafXKxVqQIxlCM85KR", outputDir="./testClass", topNResults=5, featureExt=".json", descriptors=descriptors)

# 4.2
f.classify_sound_kNN("./testClass/guitar/91199/91199_1075352-lq.json", "./testDownload", 5, descInput=[1, 12])
f.classify_sound_kNN("./testClass/guitar/110455/110455_1075352-lq.json", "./testDownload", 3, descInput=[2, 10])
f.classify_sound_kNN("./testClass/piano/673720/673720_8981843-lq.json", "./testDownload", 3, descInput = [0, 1, 14, 15])