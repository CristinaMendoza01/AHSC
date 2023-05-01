import os
import sys

import download as d
sys.path.append('./freesound-python-master/')

apiCristina = "dCvdtqvTd7A4WhnDF3qSkTZafXKxVqQIxlCM85KR"

print(os.getcwd())
#d.download_sounds_freesound("trumpet", None, None, "./src/testDownload", "dCvdtqvTd7A4WhnDF3qSkTZafXKxVqQIxlCM85KR", 10, '.json')
d.download_sounds_freesound("violin", None, None, "./src/testDownload", apiCristina, 5, '.json')
