# Base model
import numpy as np
from scipy.signal import welch
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import os
from pydub import AudioSegment
from Audio_Handler import AudioHandler
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.io import wavfile

class Spid_Model:
    #function for converting to .wav
    def __init__(self, displayer):
        self.displayer = displayer

    # changes 2-channel to 1-channel
    def channel_set(self, file_path):
        audio_handler = AudioHandler(file_path)
        exported_file = audio_handler.export()
        samplerate, data = wavfile.read(exported_file)
        if len(data.shape) > 1:
            data = data[:, 0]
        return exported_file, samplerate, data

    # waveform graph
    def waveform(self, file_path):
        exported_file, samplerate, data = self.channel_set(file_path)
        length = data.shape[0] / samplerate
        time = np.linspace(0, length, data.shape[0])

        # plot on canvas
        f = self.displayer.f
        f.clear()
        wfplot = f.add_subplot(111)
        wfplot.plot(time, data)
        wfplot.set_title("Waveform")
        wfplot.set_xlabel("Time (s)")
        wfplot.set_ylabel("Amplitude (dB)", labelpad=5)
        wfplot.tick_params(axis='y', labelsize=7)  #changing tick label size so that the y axis label fits

        # refresh canvas
        canvas = FigureCanvasTkAgg(f, self.displayer)
        canvas.draw()
        #plt.tight_layout()
        canvas.get_tk_widget().grid(row=1, column=0, columnspan=4, pady=20, sticky="w", padx=25)


    def resonance_freq(self, file_path):
        #find index of max amplitude
        exported_file, samplerate, data = self.channel_set(file_path)
        frequency, power = welch(data, samplerate, nperseg=4096)
        flat_pow = power.flatten()
        index_max = np.argmax(flat_pow)
        flat_freqs = frequency.flatten()
        dominant_freq = frequency[index_max]    #PROBLEM WITH NDARRAY
        print(f'max power: {round(dominant_freq)}')
        return dominant_freq

#print(np.__version__)