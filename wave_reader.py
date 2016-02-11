# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 17:56:46 2016

@author: Fred
"""


# Import librairies
import numpy as np
from scipy.io.wavfile import read


def wave_reader(filename):
    '''
    Read a .wav file and return a numpy array.
    '''    
    data = read(filename)
    return data[1]

wave_reader('baby.wav')