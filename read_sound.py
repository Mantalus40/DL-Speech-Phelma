import os
import wave
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import stft,istft
from sphfile import SPHFile

file_path = 'speech_TRAIN_1/TIMIT_TRAIN_1/DR1/FDAW0/SA1.wav'
folder_path = 'speech_TRAIN_1/TIMIT_TRAIN_1/DR1/FDAW0/'

# list = os.listdir(folder_path)


sph = SPHFile(file_path)
print(sph.format)
sph.write_wav( 'speech_TRAIN_1/test.wav' )

freq, sound = wavfile.read('test.wav')
print(freq)
print(sound)
# plt.plot(sound)
# plt.show()

f,t,Zxx = stft(sound,fs=freq,window='hamming',nperseg=512, noverlap=256, nfft=None, detrend=False, return_onesided=True, boundary='zeros', padded=True, axis=-1)


print(np.shape(Zxx))

Zxx_mod=np.log(np.abs(Zxx)**2)
plt.pcolormesh(t, f, Zxx_mod)
plt.show()

# t,x = istft(Zxx, fs=freq, window='hamming', nperseg=512, noverlap=256, nfft=None, input_onesided=True, boundary=True, time_axis=-1, freq_axis=-2)
#
# plt.plot(x)
# plt.show()
# print(np.shape(x))
#
# plt.plot(x[0:len(sound)]-sound)
# plt.show()