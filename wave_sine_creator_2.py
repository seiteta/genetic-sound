# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 18:45:27 2016

@author: Fred
"""

import numpy as np
from scipy.io.wavfile import write


def create_random_parameters():
    '''
        Create a dictionnary of random parameters
    '''
    parameters={}
    length = 300000
    parameters["length"] = length
    parameters["amplitude"] = (np.random.rand(1)-0.5)*2
    parameters["frequency"] = np.random.rand(1)/5.0
    parameters["phase"] = np.random.rand(1)*2*np.pi
    start = np.random.randint(0,length)
    parameters["start"] = start
    parameters["duration"] = np.random.randint(0,length-start)
    return parameters


def create_wave(parameters):
    '''
        Create a numpy array corresponding to a generated wave sine signal        

        Parameter:
        parameters => Wave sine parameters (dictionnary)
    '''
    length = parameters["length"]
    amplitude = parameters["amplitude"]
    frequency = parameters["frequency"]
    phase = parameters["phase"]
    start = parameters["start"]
    duration = parameters["duration"]
    
    empty_start = np.zeros(start)
    empty_end = np.zeros(length-duration-start)
    signal = amplitude * np.sin((2 * np.pi * frequency * np.arange(duration)) + phase)
    
    return np.hstack((empty_start,signal,empty_end))
    

def add_waves(num_waves,length):
    '''
        Add several wave sine signals.
        
        Parameters:
        num_waves => Number of added wave sines (integer)
        length => Length of the signal
    '''
    sound = np.zeros(length)
    for i in range(num_waves):
        sound = sound + create_wave(create_random_parameters())
    return sound


def write_sound (filename, soundarray):
    """
        Save a numpy array as a .wav sound file

        Parameters:
        filename => Name of the file (string)
        soundarray => Array of the sound (numpy array)
    """
    soundarray = np.int16(soundarray/np.max(np.abs(soundarray)) * 32767)
    write(filename, 44100, soundarray)
    

sound = add_waves(1000,300000)

write_sound("test.wav",sound)


