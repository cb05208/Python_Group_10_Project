# Base model
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pydub import effects
from scipy.io import wavfile
from scipy.signal import welch
from Audio_Handler import AudioHandler
import matplotlib.pyplot as plt
import ffmpeg
import os


class Spid_Model:
    def __init__(self,displayer):
        self.displayer = displayer
        self.data_in_db = -1
    # changes 2-channel to 1-channel
    def channel_set(self, file_path):
        audio_handler = AudioHandler(file_path)
        exported_file = audio_handler.export()
        samplerate, data = wavfile.read(exported_file)
        if data.ndim > 1:
            data = data[:,0]
        return exported_file, samplerate, data

    # waveform graph
    def waveform(self, file_path):
        exported_file, samplerate, data = self.channel_set(file_path)
        length = data.shape[0] / samplerate
        time = np.linspace(0,length,data.shape[0])

        #plot on canvas
        f = self.displayer.f
        f.clear()
        wfplot = f.add_subplot(111)
        wfplot.plot(time,data)
        wfplot.set_title("Waveform")
        wfplot.set_xlabel("Time (s)")
        wfplot.set_ylabel("Amplitude")
        wfplot.tick_params(axis='y', labelsize=7)

        #refresh canvas
        canvas = FigureCanvasTkAgg(f,self.displayer)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0, columnspan=4, pady=20,sticky="w",padx=25)

    def resonance_freq(self, file_path):
        #find index of max amplitude
        exported_file, samplerate, data = self.channel_set(file_path)
        frequency, power = welch(data, samplerate, nperseg=4096)
        flat_pow = power.flatten()
        index_max = np.argmax(flat_pow)
        flat_freqs = frequency.flatten()
        dominant_freq = frequency[index_max]
        print(f'max power: {round(dominant_freq)}')
        return dominant_freq

    #finds frequencies
    def find_target_frequency(self,freqs,target):
        for x in freqs:
            if x > target:
                break
        return x

    def reverb(self,file_path, target):
        exported_file, samplerate, data = self.channel_set(file_path)
        spectrum, freqs, t, im = plt.specgram(data, Fs=samplerate,
                NFFT=512, cmap=plt.get_cmap('autumn_r'),noverlap=256,mode='psd')

        def frequency_check():
            print(f'freqs {freqs[:10]}')
            target_frequency = self.find_target_frequency(freqs, target)
            print(f'target_frequency {target_frequency}')
            index_of_frequency = np.where(freqs == target_frequency)[0][0]
            print(f'index_of_frequency {index_of_frequency}')

            data_for_frequency = spectrum[index_of_frequency]
            print(f'data_for_frequency {data_for_frequency[:10]}')

            signal = np.maximum(data_for_frequency, 1e-10)
            data_in_db_fun = 10 * np.log10(signal)
            print(f"data in db fun (first 10): {data_in_db_fun[:10]}")
            return data_in_db_fun

        self.data_in_db = frequency_check()
        print(f"data_in_db {self.data_in_db}")
        return spectrum, freqs, t

    # find nearest value
    def find_nearest_value(self, array, value):
        array = np.asarray(array)
        idx = (np.abs(array - value)).argmin()
        return array[idx]

        # plot on canvas
    def frequency(self, file_path, target):
        spectrum, freqs, t = self.reverb(file_path, target)
        print(target)
        f = self.displayer.f
        f.clear()
        mfplot = f.add_subplot(111)
        mfplot.plot(t, self.data_in_db, linewidth=1, alpha=0.7,color='#004bc6')
        # mfplot.set_title("Mid RT60")
        mfplot.set_xlabel("Time (s)")
        mfplot.set_ylabel("Power (dB)")
        print(target)
        if target <= 250:
            mfplot.set_title("Low RT60 Graph")
            mfplot.plot(t, self.data_in_db, linewidth=1, alpha=0.7, color='#004bc6')
        elif target >= 5000:
            mfplot.set_title("High RT60 Graph")
            mfplot.plot(t, self.data_in_db, linewidth=1, alpha=0.7, color='red')
        else:
            mfplot.set_title("Mid RT60 Graph")
            mfplot.plot(t, self.data_in_db, linewidth=1, alpha=0.7, color='purple')

        # refresh canvas
        canvas = FigureCanvasTkAgg(f, self.displayer)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0, columnspan=4, pady=20, sticky="w", padx=25)

        # find index of max value
        index_of_max = np.argmax(self.data_in_db)
        print(f"index of max {index_of_max}")
        value_of_max = self.data_in_db[index_of_max]
        print(f"value_of_max {value_of_max}")
        mfplot.plot(t[index_of_max],self.data_in_db[index_of_max], 'go')

        # slice array from max value
        sliced_array = self.data_in_db[index_of_max:]
        value_of_max_less_than_5 = value_of_max - 5
        value_of_max_less_5 = self.find_nearest_value(sliced_array, value_of_max_less_than_5)
        index_of_max_less_5 = np.where(self.data_in_db == value_of_max_less_5)
        mfplot.plot(t[index_of_max_less_5], self.data_in_db[index_of_max_less_5], 'yo')

        #slice array from max -5dB
        value_of_max_less_25 = value_of_max - 25
        value_of_max_less_25 = self.find_nearest_value(sliced_array, value_of_max_less_25)
        index_of_max_less_25 = np.where(self.data_in_db == value_of_max_less_25)
        mfplot.plot(t[index_of_max_less_25], self.data_in_db[index_of_max_less_25], 'ro')
        rt60 = (t[index_of_max_less_5] - t[index_of_max_less_25])[0]

        #extrapolate rt20 to rt60
        print(f'The RT60 reverb time is {round(abs(rt60),2)} seconds')
        return abs(rt60)
