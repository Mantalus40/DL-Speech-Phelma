import os
import wave
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import stft,istft
import random
from playsound import playsound
import math as m

## Chargement des sons
freq_b, bruit = wavfile.read('babble.wav')

f1,son1 = wavfile.read('speech_TRAIN_1/TIMIT_TRAIN_1_WAV/DR1/FCJF0/SA1.wav')

print("f1",f1)
print("longueur son 1 : ",len(son1))

N = len(son1)

## Normalisation
bruit = (bruit-np.mean(bruit))/m.sqrt(np.var(bruit))
son1 = (son1-np.mean(son1))/m.sqrt(np.var(son1))

## Sélection de la fenêtre de bruit
a = random.randint(0,len(bruit)-len(son1)-1)
b = a + len(son1)
short_bruit = bruit[a:b]

## Génération du signal bruité avec RSB de 0dB
Ps=np.sum(son1**2) #puissance du signal
Pb=np.sum(short_bruit**2) #puissance du bruit
son1_bruit = son1 + (Ps/Pb)*short_bruit #signal bruité avec un RSB de 0 dB

plt.plot(bruit)
plt.show()
## Enregistrement du signal bruité
wavfile.write('son1.wav',f1,son1_bruit)

# playsound('son2.wav')

## Affichage des spectrogrammes
f,t,Zxx = stft(son1,fs=f1,window='hamming',nperseg=512, noverlap=256, nfft=None, detrend=False, return_onesided=True, boundary='zeros', padded=True, axis=-1)

Zxx=np.log(np.abs(Zxx)**2)
plt.subplot(121)
plt.pcolormesh(t, f, Zxx)


f_bruit,t_bruit,Zxx_bruit = stft(son1_bruit,fs=f1,window='hamming',nperseg=512, noverlap=256, nfft=None, detrend=False, return_onesided=True, boundary='zeros', padded=True, axis=-1)

Zxx_bruit=np.log(np.abs(Zxx_bruit)**2)
plt.subplot(122)
plt.pcolormesh(t_bruit, f_bruit, Zxx_bruit)
plt.show()