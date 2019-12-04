import os
import wave
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import stft,istft
import random
import math as m
from path import Path


freq_b, bruit = wavfile.read('babble.wav')


for file_path in Path('speech_TEST/TIMIT_TEST_WAV').walkfiles('*.WAV'):

    save_path = os.path.dirname(os.path.dirname(os.path.dirname(file_path))) + '_NOISED/' + os.path.basename(os.path.dirname(os.path.dirname(file_path))) + '/' + os.path.basename(os.path.dirname(file_path))+ '/'+os.path.basename(file_path)

    try:
        if not os.path.exists(os.path.dirname(save_path)):
            os.makedirs(os.path.dirname(save_path))
    except OSError:
        print ('Error: Creating directory of data')

    f,s = wavfile.read( file_path )

    bruit = (bruit-np.mean(bruit))/m.sqrt(np.var(bruit))
    s = (s-np.mean(s))/m.sqrt(np.var(s))

    a = random.randint(0,len(bruit)-len(s)-1)
    b = a + len(s)
    short_bruit = bruit[a:b]

    Ps=np.sum(s**2) #puissance du signal
    Pb=np.sum(short_bruit**2) #puissance du bruit
    s_bruit = s + (Ps/Pb)*short_bruit #signal bruité avec un RSB de 0 dB

    wavfile.write(save_path,f,s_bruit)
