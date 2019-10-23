import os
import wave
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from sphfile import SPHFile

file_path = 'speech_TEST/TIMIT_TEST/DR1/FAKS0/SA1.wav'
folder_path = 'speech_TEST/TIMIT_TEST/DR1/FAKS0/'

list = os.listdir(folder_path)


sph = SPHFile(file_path)
print(sph.format)
sph.write_wav( 'test.wav' )

freq, sound = wavfile.read('test.wav')
print(freq)
print(sound)
plt.plot(sound)
plt.show()

#
# wav = wave.open('test.wav')
# rate = wav.getframerate()
# nchannels = wav.getnchannels()
# sampwidth = wav.getsampwidth()
# nframes = wav.getnframes()
# data = wav.readframes(nframes)
# wav.close()
# array = _wav2array(nchannels, sampwidth, data)