import os
import wave
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import stft,istft
import random
import math as m
from path import Path


clean_spectrogrammes = []
noised_spectrogrammes = []
name_clean_spectrogrammes = []
name_noised_spectrogrammes = []


for file_path in Path('speech_TRAIN_1/TIMIT_TRAIN_1_WAV').walkfiles('*.WAV'):

    print(file_path)
    freq,sound = wavfile.read( file_path )
    sound = (sound-np.mean(sound))/m.sqrt(np.var(sound))

    f,t,Zxx = stft(sound,fs=freq,window='hamming',nperseg=512, noverlap=256, nfft=None, detrend=False, return_onesided=True, boundary='zeros', padded=True, axis=-1)

    Zxx=np.log(np.abs(Zxx)**2)
    clean_spectrogrammes.append(Zxx)
    name_clean_spectrogrammes.append(file_path)


for file_path in Path('speech_TRAIN_2/TIMIT_TRAIN_2_WAV').walkfiles('*.WAV'):

    print(file_path)
    freq,sound = wavfile.read( file_path )
    sound = (sound-np.mean(sound))/m.sqrt(np.var(sound))

    f,t,Zxx = stft(sound,fs=freq,window='hamming',nperseg=512, noverlap=256, nfft=None, detrend=False, return_onesided=True, boundary='zeros', padded=True, axis=-1)

    Zxx=np.log(np.abs(Zxx)**2)
    clean_spectrogrammes.append(Zxx)
    name_clean_spectrogrammes.append(file_path)

for file_path in Path('speech_TRAIN_1/TIMIT_TRAIN_1_WAV_NOISED').walkfiles('*.WAV'):

    print(file_path)
    freq,sound = wavfile.read( file_path )
    sound = (sound-np.mean(sound))/m.sqrt(np.var(sound))

    f,t,Zxx = stft(sound,fs=freq,window='hamming',nperseg=512, noverlap=256, nfft=None, detrend=False, return_onesided=True, boundary='zeros', padded=True, axis=-1)

    Zxx=np.log(np.abs(Zxx)**2)
    noised_spectrogrammes.append(Zxx)
    name_noised_spectrogrammes.append(file_path)

for file_path in Path('speech_TRAIN_2/TIMIT_TRAIN_2_WAV_NOISED').walkfiles('*.WAV'):

    print(file_path)
    freq,sound = wavfile.read( file_path )
    sound = (sound-np.mean(sound))/m.sqrt(np.var(sound))

    f,t,Zxx = stft(sound,fs=freq,window='hamming',nperseg=512, noverlap=256, nfft=None, detrend=False, return_onesided=True, boundary='zeros', padded=True, axis=-1)

    Zxx=np.log(np.abs(Zxx)**2)
    noised_spectrogrammes.append(Zxx)
    name_noised_spectrogrammes.append(file_path)