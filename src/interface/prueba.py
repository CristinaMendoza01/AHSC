import urllib.request
from finalGUI import mp3towav
from soundImprover import  improveSound
sound = "https://cdn.freesound.org/previews/519/519019_11454468-hq.mp3"
sound_url = sound
store_name1 = sound_url.split('/')[-1]
sound_dir = "../dataset/" + store_name1
urllib.request.urlretrieve(sound_url, sound_dir)
store_name2 = mp3towav(store_name1)
sound_dir2 = "../dataset/" + store_name2
improveSound(sound_dir, sound_dir2)
urllib.request.urlretrieve(sound_url, sound_dir2)

# urllib.request.urlretsrieve("https://cdn.freesound.org/previews/519/519019_11454468-hq.mp3", "../dataset/519019_11454468-hq.mp3")