import shutil
import tkinter as tk
import wave

import simpleaudio as sa
import soundfile


# def reproducir_sonido():
#     wave_obj = sa.WaveObject.from_wave_file('hi.wav')
#     play_obj = wave_obj.play()

def improveSound(oldSound, newSound):
    shutil.copy(oldSound, newSound)

    # Read and rewrite the file with soundfile
    data, samplerate = soundfile.read(newSound)
    soundfile.write(newSound, data, samplerate)

    # Now try to open the file with wave
    with wave.open(newSound) as file:
        print('File opened!')

# improveSound("hi.mp3", "hi.wav")