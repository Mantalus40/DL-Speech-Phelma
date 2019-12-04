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
f2,son2 = wavfile.read('speech_TRAIN_2/TIMIT_TRAIN_2_WAV/DR5/FBJL0/SA1.wav')

print("f1",f1)
print("longueur son 1 : ",len(son1))

N = len(son1)
M = len(son2)

## Normalisation
bruit = (bruit-np.mean(bruit))/m.sqrt(np.var(bruit))
son1 = (son1-np.mean(son1))/m.sqrt(np.var(son1))
son2 = (son2-np.mean(son2))/m.sqrt(np.var(son2))

## Sélection de la fenêtre de bruit
a = random.randint(0,len(bruit)-len(son1)-1)
b = a + len(son1)
short_bruit1 = bruit[a:b]

c = random.randint(0,len(bruit)-len(son2)-1)
d = c + len(son2)
short_bruit2 = bruit[c:d]

## Génération du signal bruité avec RSB de 0dB
Ps1=np.sum(son1**2) #puissance du signal
Ps2=np.sum(son2**2)
Pb1=np.sum(short_bruit1**2) #puissance du bruit
Pb2=np.sum(short_bruit2**2)
son1_bruit = son1 + (Ps1/Pb1)*short_bruit1 #signal bruité avec un RSB de 0 dB
son2_bruit = son2 + (Ps2/Pb2)*short_bruit2

plt.plot(bruit)
plt.show()
## Enregistrement du signal bruité
wavfile.write('son1.wav',f1,son1_bruit)

# playsound('son2.wav')

## Affichage des spectrogrammes
f,t,Zxx = stft(son1,fs=f1,window='hamming',nperseg=512, noverlap=256, nfft=None, detrend=False, return_onesided=True, boundary='zeros', padded=True, axis=-1)

f_2,t_2,Zxx_2 = stft(son2,fs=f2,window='hamming',nperseg=512, noverlap=256, nfft=None, detrend=False, return_onesided=True, boundary='zeros', padded=True, axis=-1)

Zxx=np.log(np.abs(Zxx)**2)
plt.subplot(141)
plt.pcolormesh(t, f, Zxx)
plt.subplot(142)
plt.pcolormesh(Zxx)

f_bruit,t_bruit,Zxx_bruit = stft(son1_bruit,fs=f1,window='hamming',nperseg=512, noverlap=256, nfft=None, detrend=False, return_onesided=True, boundary='zeros', padded=True, axis=-1)

f_bruit_2,t_bruit_2,Zxx_bruit_2 = stft(son2_bruit,fs=f2,window='hamming',nperseg=512, noverlap=256, nfft=None, detrend=False, return_onesided=True, boundary='zeros', padded=True, axis=-1)

Zxx_bruit=np.log(np.abs(Zxx_bruit)**2)
plt.subplot(143)
plt.pcolormesh(t_bruit, f_bruit, Zxx_bruit)
plt.subplot(144)
plt.pcolormesh(Zxx_bruit)
plt.show()