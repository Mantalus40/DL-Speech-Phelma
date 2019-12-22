import os
import wave
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import stft,istft
import random
import math as m
from path import Path


max_len = 0
min_len = 120000
mean = 10000
#
# name_clean_spectrogrammes = []
# name_noised_spectrogrammes = []
clean_spectrogrammes = np.empty([257,197,1])
noised_spectrogrammes = np.empty([257,197,1])
test_clean_spectrogrammes = np.empty([257,197,1])
test_noised_spectrogrammes = np.empty([257,197,1])

## Compute max length within all sounds
for file_path in Path('speech_TRAIN_1/TIMIT_TRAIN_1_WAV').walkfiles('*.WAV'):

    f,s = wavfile.read( file_path )

    if len(s)>max_len:
        max_len = len(s)
    if len(s)<min_len:
        min_len = len(s)
    mean = (mean+len(s))/2

for file_path in Path('speech_TRAIN_2/TIMIT_TRAIN_2_WAV').walkfiles('*.WAV'):

    f,s = wavfile.read( file_path )

    if len(s)>max_len:
        max_len = len(s)
    if len(s)<min_len:
        min_len = len(s)
    mean = (mean+len(s))/2

## Zero-pad noised sound
mean = 50000

for file_path in Path('speech_TRAIN_1/TIMIT_TRAIN_1_WAV').walkfiles('*.WAV'):

    print( file_path )
    f,s = wavfile.read( file_path )
    s = (s-np.mean(s))/m.sqrt(np.var(s))
    if len(s)<mean:
         s = np.concatenate((s,np.zeros(mean-len(s))))
    else:
        s = s[0:mean]

    freq,time,spec = stft(s,fs=f,window='hamming',nperseg=512, noverlap=256, nfft=None, detrend=False, return_onesided=True, boundary='zeros', padded=True, axis=-1)

    spec=np.log(np.abs(spec)**2)
    clean_spectrogrammes = np.dstack([clean_spectrogrammes,spec])
    # name_clean_spectrogrammes.append(file_path)

#
for file_path in Path('speech_TRAIN_1/TIMIT_TRAIN_1_WAV_NOISED').walkfiles('*.WAV'):

    print( file_path )
    f,s = wavfile.read( file_path )
    if len(s)<mean:
         s = np.concatenate((s,np.zeros(mean-len(s))))
    else:
        s = s[0:mean]

    freq,time,spec = stft(s,fs=f,window='hamming',nperseg=512, noverlap=256, nfft=None, detrend=False, return_onesided=True, boundary='zeros', padded=True, axis=-1)

    spec=np.log(np.abs(spec)**2)
    noised_spectrogrammes = np.dstack([noised_spectrogrammes,spec])
    # name_noised_spectrogrammes.append(file_path)

#
# for file_path in Path('speech_TRAIN_2/TIMIT_TRAIN_2_WAV').walkfiles('*.WAV'):
#
#     print( file_path )
#     f,s = wavfile.read( file_path )
#     # if len(s)<max_len:
#     #      s = np.concatenate((s,np.zeros(max_len-len(s))))
#
#     s = s[0:min_len-1]
#
#     freq,time,spec = stft(s,fs=f,window='hamming',nperseg=512, noverlap=256, nfft=None, detrend=False, return_onesided=True, boundary='zeros', padded=True, axis=-1)
#
#     spec=np.log(np.abs(spec)**2)
#     clean_spectrogrammes = np.dstack([clean_spectrogrammes,spec])
#     name_clean_spectrogrammes.append(file_path)
#
#
# for file_path in Path('speech_TRAIN_2/TIMIT_TRAIN_2_WAV_NOISED').walkfiles('*.WAV'):
#
#     print( file_path )
#     f,s = wavfile.read( file_path )
    # if len(s)<max_len:
    #      s = np.concatenate((s,np.zeros(max_len-len(s))))

#     s = s[0:min_len-1]
#
#     freq,time,spec = stft(s,fs=f,window='hamming',nperseg=512, noverlap=256, nfft=None, detrend=False, return_onesided=True, boundary='zeros', padded=True, axis=-1)
#
#     spec=np.log(np.abs(spec)**2)
#     noised_spectrogrammes = np.dstack([noised_spectrogrammes,spec])
#     name_clean_spectrogrammes.append(file_path)
#
for file_path in Path('speech_TEST/TIMIT_TEST_WAV').walkfiles('*.WAV'):

    print( file_path )
    f,s = wavfile.read( file_path )
    if len(s)<mean:
         s = np.concatenate((s,np.zeros(mean-len(s))))
    else:
        s = s[0:mean]

    freq,time,spec = stft(s,fs=f,window='hamming',nperseg=512, noverlap=256, nfft=None, detrend=False, return_onesided=True, boundary='zeros', padded=True, axis=-1)

    spec=np.log(np.abs(spec)**2)
    test_clean_spectrogrammes = np.dstack([test_clean_spectrogrammes,spec])
#
for file_path in Path('speech_TEST/TIMIT_TEST_WAV_NOISED').walkfiles('*.WAV'):

    print( file_path )
    f,s = wavfile.read( file_path )
    if len(s)<mean:
         s = np.concatenate((s,np.zeros(mean-len(s))))
    else:
        s = s[0:mean]

    freq,time,spec = stft(s,fs=f,window='hamming',nperseg=512, noverlap=256, nfft=None, detrend=False, return_onesided=True, boundary='zeros', padded=True, axis=-1)

    spec=np.log(np.abs(spec)**2)
    test_noised_spectrogrammes = np.dstack([test_noised_spectrogrammes,spec])