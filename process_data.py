import os
import wave
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from sphfile import SPHFile

path = '/home/user/Documents/SICOM3/audio/test'
i=0
files = []
r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.WAV' in file:
            files.append(os.path.join(r, file))

for f in files:\n",
    print(f)\n",
    src=f
    dst=\"T\"+str(i)+\".wav\"
    os.rename(src,dst)
    i+=1