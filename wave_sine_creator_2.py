# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 18:45:27 2016

@author: Fred
"""
import numpy as np
from scipy.io.wavfile import write,read

def create_random_parameters():
    '''
        Create a dictionnary of random parameters
    '''
    parameters = np.random.rand(5)
    min_amplitude = 1
    max_amplitude = 200 #TODO: use max(target_sound)/number_of_wave
    # frequency range: from 20 000 Hz to 20 Hz
    min_frequency = 1/20000.0
    max_frequency = 1/20.0
    min_phase = 0
    max_phase = 2 * np.pi
    min_start = 0
    max_start = length
    parameters[0] = (parameters[0] * (max_amplitude-min_amplitude)) + min_amplitude
    parameters[1] = (parameters[1] * (max_frequency-min_frequency)) + min_frequency
    parameters[2] = (parameters[2] * (max_phase-min_phase)) + min_phase
    parameters[3] = int((parameters[3] * (max_start-min_start)) + min_start)
    min_duration = 0
    max_duration = length-parameters[3]  
    parameters[4] = int((parameters[4] * (max_duration-min_duration)) + min_duration)
    return parameters


def create_wave(parameters):
    '''
        Create a numpy array corresponding to a generated wave sine signal        

        Parameter:
        parameters => Wave sine parameters (dictionnary)
    '''
    amplitude = parameters[0]
    frequency = parameters[1]
    phase = parameters[2]
    start = parameters[3]
    duration = parameters[4]
    
    empty_start = np.zeros(start)
    empty_end = np.zeros(length-duration-start)
    signal = amplitude * np.sin((2 * np.pi * frequency * np.arange(duration)) + phase)
    
    return np.hstack((empty_start,signal,empty_end))
    

def add_waves(num_waves):
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
    

def wave_reader(filename):
    '''
    Read a .wav file and return a numpy array.
    '''    
    data = read(filename)
    return data[1]

def compute_loss(prediction, target):
    n = len(prediction)
    rmse = np.linalg.norm(prediction - target) / np.sqrt(n)
    return rmse

target_sound = wave_reader('baby.wav')
length = len(target_sound)

generated_sound = add_waves(10000)

loss = compute_loss(generated_sound,target_sound)
print loss

write_sound("test.wav",generated_sound)









