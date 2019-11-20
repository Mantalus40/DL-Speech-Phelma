import os
import wave
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from sphfile import SPHFile
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=100))
model.add(Dense(units=10, activation='softmax'))

model.compile(loss='categorical_crossentropy',
optimizer='sgd',
metrics=['accuracy'])