# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 18:45:27 2016

@author: Fred
"""
import numpy as np
from scipy.io.wavfile import write,read


num_waves = 100
gen_size = 10

def transform_parameter(parameters):
    '''
    '''
    new_range_parameters = np.zeros(5)       
    min_amplitude = 1
    max_amplitude = 200 #TODO: use max(target_sound)/number_of_wave
    # frequency range: from 20 000 Hz to 20 Hz
    min_frequency = 1/20000.0
    max_frequency = 1/20.0
    min_phase = 0
    max_phase = 2 * np.pi
    min_start = 0
    max_start = length
    new_range_parameters[0] = (parameters[0] * (max_amplitude-min_amplitude)) + min_amplitude
    new_range_parameters[1] = (parameters[1] * (max_frequency-min_frequency)) + min_frequency
    new_range_parameters[2] = (parameters[2] * (max_phase-min_phase)) + min_phase
    new_range_parameters[3] = int((parameters[3] * (max_start-min_start)) + min_start)
    min_duration = 0
    max_duration = length-new_range_parameters[3]  
    new_range_parameters[4] = int((parameters[4] * (max_duration-min_duration)) + min_duration)
    return new_range_parameters


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
    
def add_waves(in_parameters):
    '''
        Add several wave sine signals.
        
        Parameters:
        num_waves => Number of added wave sines (integer)
    '''
    sound = np.zeros(length)
    for i in range(num_waves):
        in_parameters = np.random.rand(5)
        parameters = transform_parameter(in_parameters)
        sound = sound + create_wave(parameters)
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
    '''Compute the root mean square error (RMSE) between two arrays
    
    Parameters
    ----------
    prediction => Generated sound (numpy array)
    traget => Read soud (numpy array)

    Returns
    -------
    rmse => Root mean square error (float)

    
    '''
    n = len(prediction)
    rmse = np.linalg.norm(prediction - target) / np.sqrt(n)
    return rmse



target_sound = wave_reader('baby.wav')
length = len(target_sound)



def initialize(gen_size,num_waves):
    pop_parameters=np.zeros((gen_size,5))
    losses = np.zeros((gen_size,1))
    for i in range(gen_size):
        initial_parameters = np.random.rand(5)
        generated_sound = add_waves(initial_parameters)
        pop_parameters[i] = initial_parameters
        losses[i] = compute_loss(generated_sound,target_sound)
    best_individual_index = np.argmin(losses)
    best_individual_parameters = pop_parameters[best_individual_index]
    return best_individual_parameters, losses[best_individual_index]


def new_generation(best_individual_parameters,best_loss):

    pop_parameters=np.zeros((gen_size,5))
    losses = np.zeros((gen_size,1))
    pop_parameters[0] = best_individual_parameters
    losses[0] = best_loss
    
    for i in range(gen_size-1):
        mutation = np.random.rand(5)*np.random.randint(2, size=5)
        new_individual_parameters = best_individual_parameters + mutation
        pop_parameters[i+1] = new_individual_parameters
        generated_sound = add_waves(new_individual_parameters)
        losses[i+1] = compute_loss(generated_sound,target_sound) #Useless computation of best_individual_parameters loss    
    
    best_individual_index = np.argmin(losses)
    best_individual_parameters = pop_parameters[best_individual_index]
    
    print(best_individual_parameters)
    print(losses[best_individual_index])
    
    if losses[best_individual_index]>1000:        
        return new_generation(best_individual_parameters, losses[best_individual_index])
    else:
        return best_individual_parameters, losses[best_individual_index]


#init_param, init_loss = initialize(gen_size,num_waves)
#new_generation(init_param,init_loss)


#generated_sound,parameters = add_waves(100)

#loss = compute_loss(generated_sound,target_sound)
#print loss

#write_sound("test.wav",generated_sound)










