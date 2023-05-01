import os
import sys

import download as d
sys.path.append('./freesound-python-master/')

print(os.getcwd())
d.download_sounds_freesound("trumpet", "./src/testDownload", "dCvdtqvTd7A4WhnDF3qSkTZafXKxVqQIxlCM85KR", 5, '.json')
