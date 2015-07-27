# -*- coding: utf-8 -*-
"""
Main.

@author: Agnieszka Kaczmarczyk
"""

import matplotlib.pyplot as plt
import numpy as np
import wave_operations as wo
import preprocessing as pr
import segmentation as segm
import threshold
import s12_determinator as s12
from parametrization import Parameters
import os
from os import listdir
from os.path import isfile, join

plt.close('all')
freq = 4000

my_path = os.getcwd() + '\\normal signals'
wave_files = [ f for f in listdir(my_path) if isfile(join(my_path,f)) ]

for wave_file in wave_files[0:1]:
    wave_file_path = my_path + '\\' + wave_file
    print wave_file_path
    signal_PCG, params = wo.read_wavefile(wave_file_path)
    # Preprocessing of the signal: decimation.
    signal_PCG = pr.decimate(signal_PCG, params, freq)
    
    # Preprocessing of the signal: normalization.
    signal_PCG = pr.normalize(signal_PCG)
    
    signal_PCG_original = np.copy(signal_PCG)
    
    # Preprocessing of the signal: filtering.
    cutoff = 100
    signal_PCG = pr.butter_lowpass_filter(signal_PCG, cutoff, freq, 1)
    
    # Denoising histogram using histogram method.
    signal_PCG = segm.histogram_denoising(signal_PCG)
    
    # Determine heart rate.
    heart_rate = segm.heart_rate(signal_PCG, freq) 

    # Shannon energy envelope
    shannon_envelope = segm.envelope(signal_PCG, freq)
    
    thr, starts, stops, heart_rate, peaks_energy = threshold.determine_threshold(shannon_envelope, freq, heart_rate)
    
    boundaries = s12.find_cycle_start(signal_PCG, starts, heart_rate, freq)   
    s1, s2 = s12.determine_s12(starts, stops, boundaries, peaks_energy)
    
    parameters = Parameters(signal_PCG_original, freq, heart_rate, s1, s2, starts, stops)      
    
    T = 1.0/freq
    length = len(signal_PCG)
    t = np.arange(0, length, 1)
    t = t * T
    f, axarr = plt.subplots(3, sharex=True)
    axarr[1].plot(t, signal_PCG)
    axarr[0].plot(t, signal_PCG_original)
    axarr[0].set_title(wave_file + ' ' + str(heart_rate))
    for boundary in boundaries:
        axarr[0].axvline(boundary * 1.0/ freq, color = 'red') 
    for index in s1:
        axarr[0].axvline(starts[index] * 1.0/ freq, color = 'green')
        axarr[0].axvline(stops[index] * 1.0/ freq, color = 'green')
    for index in s2:
        axarr[0].axvline(starts[index] * 1.0/ freq, color = 'yellow')
        axarr[0].axvline(stops[index] * 1.0/ freq, color = 'yellow')
    axarr[2].plot(t, shannon_envelope)

#    plt.savefig('plots normal\\' + wave_file[0:len(wave_file) - 4] + '.png')
#    plt.close()

#####################################################

my_path = os.getcwd() + '\\murmurs'
wave_files = [ fi for fi in listdir(my_path) if isfile(join(my_path,fi)) ]

for wave_file in wave_files[0:0]:
    wave_file_path = my_path + '\\' + wave_file
    print wave_file_path
    signal_PCG, params = wo.read_wavefile(wave_file_path)
    # Preprocessing of the signal: decimation.
    signal_PCG = pr.decimate(signal_PCG, params, freq)
    
    # Preprocessing of the signal: normalization.
    signal_PCG = pr.normalize(signal_PCG)
    
    signal_PCG_original = np.copy(signal_PCG)
    
    # Preprocessing of the signal: filtering.
    cutoff = 100
    signal_PCG = pr.butter_lowpass_filter(signal_PCG, cutoff, freq, 1)
    
    # Denoising histogram using histogram method.
    signal_PCG = segm.histogram_denoising(signal_PCG)
    
    # Determine heart rate.
    heart_rate = segm.heart_rate(signal_PCG, freq) 

    # Shannon energy envelope
    shannon_envelope = segm.envelope(signal_PCG, freq)
    
    thr, starts, stops, heart_rate, peaks_en = threshold.determine_threshold(shannon_envelope, freq, heart_rate)
    
    boundaries = s12.find_cycle_start(signal_PCG, starts, heart_rate, freq)   
    s1, s2 = s12.determine_s12(starts, stops, boundaries, peaks_en)
    
    T = 1.0/freq
    length = len(signal_PCG)
    t = np.arange(0, length, 1)
    t = t * T
    f, axarr = plt.subplots(3, sharex=True)
    axarr[1].plot(t, signal_PCG)
    axarr[0].plot(t, signal_PCG_original)
    axarr[0].set_title(wave_file + ' ' + str(heart_rate))
    for boundary in boundaries:
        axarr[0].axvline(boundary * 1.0/ freq, color = 'red') 
    for index in s1:
        axarr[0].axvline(starts[index] * 1.0/ freq, color = 'green')
        axarr[0].axvline(stops[index] * 1.0/ freq, color = 'green')
    for index in s2:
        axarr[0].axvline(starts[index] * 1.0/ freq, color = 'yellow')
        axarr[0].axvline(stops[index] * 1.0/ freq, color = 'yellow')
    axarr[2].plot(t, shannon_envelope)
    
#    plt.savefig('plots murmurs\\' + wave_file[0:len(wave_file) - 4] + '.png')
#    plt.close()

###############################################################################

my_path = os.getcwd() + '\\extrahs'
wave_files = [ fi for fi in listdir(my_path) if isfile(join(my_path,fi)) ]

for wave_file in wave_files[0:0]:
    wave_file_path = my_path + '\\' + wave_file
    print wave_file_path
    signal_PCG, params = wo.read_wavefile(wave_file_path)
    # Preprocessing of the signal: decimation.
    signal_PCG = pr.decimate(signal_PCG, params, freq)
    
    # Preprocessing of the signal: normalization.
    signal_PCG = pr.normalize(signal_PCG)
    
    signal_PCG_original = np.copy(signal_PCG)
    
    # Preprocessing of the signal: filtering.
    cutoff = 100
    signal_PCG = pr.butter_lowpass_filter(signal_PCG, cutoff, freq, 1)
    
    # Denoising histogram using histogram method.
    signal_PCG = segm.histogram_denoising(signal_PCG)
    
    # Determine heart rate.
    heart_rate = segm.heart_rate(signal_PCG, freq) 

    # Shannon energy envelope
    shannon_envelope = segm.envelope(signal_PCG, freq)
    
    thr, starts, stops, heart_rate, peaks_en = threshold.determine_threshold(shannon_envelope, freq, heart_rate)
    
    boundaries = s12.find_cycle_start(signal_PCG, starts, heart_rate, freq)   
    s1, s2 = s12.determine_s12(starts, stops, boundaries, peaks_en)
    
    T = 1.0/freq
    length = len(signal_PCG)
    t = np.arange(0, length, 1)
    t = t * T
    f, axarr = plt.subplots(3, sharex=True)
    axarr[1].plot(t, signal_PCG)
    axarr[0].plot(t, signal_PCG_original)
    axarr[0].set_title(wave_file + ' ' + str(heart_rate))
    for boundary in boundaries:
        axarr[0].axvline(boundary * 1.0/ freq, color = 'red') 
    for index in s1:
        axarr[0].axvline(starts[index] * 1.0/ freq, color = 'green')
        axarr[0].axvline(stops[index] * 1.0/ freq, color = 'green')
    for index in s2:
        axarr[0].axvline(starts[index] * 1.0/ freq, color = 'yellow')
        axarr[0].axvline(stops[index] * 1.0/ freq, color = 'yellow')
    axarr[2].plot(t, shannon_envelope)
    
    plt.savefig('plots extrahs\\' + wave_file[0:len(wave_file) - 4] + '.png')
    plt.close()

