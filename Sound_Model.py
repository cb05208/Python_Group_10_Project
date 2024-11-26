# Base model
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.io import wavfile
from Audio_Handler import AudioHandler

class Spid_Model:
    def __init__(self,displayer):
        self.displayer = displayer
    # changes 2-channel to 1-channel
    def channel_set(self, file_path):
        audio_handler = AudioHandler(file_path)
        exported_file = audio_handler.export()
        samplerate, data = wavfile.read(exported_file)
        if len(data.shape) > 1:
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

        #refresh canvas
        canvas = FigureCanvasTkAgg(f,self.displayer)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0, columnspan=4, pady=20,sticky="w",padx=25)

