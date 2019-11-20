import os
import sys
#sys.path.append("tracker/deep_sort/deep_sort")
import numpy as np
from path import Path


for file_path in Path('speech_TRAIN_1/TIMIT_TRAIN_1').walkfiles('*.WAV'):

    save_path = os.path.dirname(os.path.dirname(os.path.dirname(file_path))) + '_WAV/' + os.path.basename(os.path.dirname(os.path.dirname(file_path))) + '/' + os.path.basename(os.path.dirname(file_path))+ '/'+os.path.basename(file_path)

    try:
        if not os.path.exists(os.path.dirname(save_path)):
            os.makedirs(os.path.dirname(save_path))
    except OSError:
        print ('Error: Creating directory of data')

    sph = SPHFile(file_path)
    sph.write_wav( save_path )


