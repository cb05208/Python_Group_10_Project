# Base model
import numpy as np
from scipy.signal import welch
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import os
from pydub import AudioSegment

class Spid_Model:
    #function for converting to .wav
    def convert_m4a_to_wav(self, _file):
        #should maybe be called even if .wav
        audio = AudioSegment.from_file(_file, format = "m4a")
        audio.export(audio, format = "wav") #turns audio into wav file

    #waveform function

    #find target frequency