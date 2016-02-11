# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 17:56:46 2016

@author: Fred
"""


# Import librairies
import numpy as np
from scipy.io.wavfile import write

# Generate a random array (44100 random samples between -1 and 1)
data = np.random.uniform(-1,1,44100)

# No idea what this line does...
scaled = np.int16(data/np.max(np.abs(data)) * 32767)


def WriteSound (filename, soundArray):
    """
        Takes a numpy array and save it as a wav sound file
        Parameters:
        filename => Name of the file (string)
        soundArray => Array of the sound (numpy array)
    """
    # Write the .wav file
    write(filename, 44100, soundArray)