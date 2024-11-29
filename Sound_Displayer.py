# Base UI
from tkinter import *
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import filedialog
from Audio_Handler import AudioHandler

# Set up main windoww
class Spid_Displayer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Interactive Data Acoustic Modeling")
        self.geometry("725x700")
        self.config(pady=10)
        self.minsize(725,700)

        self.audio_handler = None
        self.spid_model = None
        self.create_buttons()

        self.mainloop()

    def create_buttons(self):
        from Sound_Model import Spid_Model
        wf = Spid_Model.waveform

        # Choose file button
        s = ttk.Style(self)
        s.configure('TButton',font=('Arial',12))
        self._file_btn = ttk.Button(
            self, text="Pick File",style="TButton",command=self.get_file,padding="10 10 10 10")
        self._file_btn.grid(row=0,column=0,padx=25,pady=10,
                        sticky='w')

        # File label
        self._file_frame = ttk.Label(
            self, text="filename.wav",
            font=10)
        self._file_frame.grid(row=0, column=1, sticky='w')

        # Analyze file button
        self._analyze_btn = ttk.Button(
            self, text="Analyze File",style="TButton",padding="10 10 10 10")
        self._analyze_btn.grid(row=0,column=2,pady=10,padx=155, sticky='e')

        # Initial plot
        self.f = Figure(figsize=(6,4), dpi=100)
        self.plot1 = self.f.add_subplot(111)
        self.plot1.set_title('Default Graph')
        canvas = FigureCanvasTkAgg(self.f, self)
        canvas.draw()
        #CHECK
        #canvas.get_tk_widget().pack(expand = 1)
        canvas.get_tk_widget().grid(row=1,column=0,columnspan=4,pady=20,
                                    sticky='w', padx=25)

        # File length label
        self._file_length = ttk.Label(
            self,text="File Length: 0s",font=('Arial',12),borderwidth=5,
            padding= '10 10 10 10',relief="groove")
        self._file_length.grid(row=2,column=0,padx=25,pady=10,sticky='w')

        # Resonance freq label
        self._file_freq = ttk.Label(
            self,text="Resonance Frequency: ___ Hz",font=('Arial',12),
            borderwidth=5, padding= '10 10 10 10',relief="groove")
        self._file_freq.grid(row=3,column=0,padx=25,pady=10,sticky='w',
                        columnspan=2)

        # RT60 difference label
        self._file_rtDiff = ttk.Label(
            self, text="RT60 Difference: _._s",font=('Arial',12),
            borderwidth=5, padding= '10 10 10 10',relief="groove")
        self._file_rtDiff.grid(row=4,column=0,padx=25,pady=10)

        # Waveform plot button
        self._waveform_btn = ttk.Button(
            self, text="Waveform",style="TButton",command=self.plot_waveform,padding="8 8 8 8")
        self._waveform_btn.grid(row=2,column=2,pady=10,sticky="w")

        # Special plot button
        self.special_btn = ttk.Button(
            self, text="Special",style="TButton",padding="8 8 8 8")
        self.special_btn.grid(row=3,column=2,pady=10,sticky="w")

        # RT plot dropdown
        options = [" Low", " Medium", " High"]
        rt_in = StringVar()
        rt_in.set("RT Plots")
        rt_combobox = ttk.Combobox(self, state="readonly", values=options,
                        width=11,font=('Arial',12))
        rt_combobox.set("     RT Plots")
        rt_combobox.grid(row=2,column=2,pady=10,ipady=7)

        # Combine plots button
        self.combPlots_btn = ttk.Button(
            self, text="Combine Plots",style="TButton",padding="8 8 8 8")
        self.combPlots_btn.grid(row=3,column=2,pady=10)


        #creating scrollbar
        #CHECK, DO LATER DOESNT WORK NOW, NEED TO ADD BUTTONS TO A SECOND FRAME ON TOP OF MAIN FRAME FOR SCROLL TO WORK
        #scroll_bar = ttk.Scrollbar(tk.Tk, orient=VERTICAL, command=canvas.get_tk_widget().yview)
        #scroll_bar.pack(side=RIGHT, fill=Y)
        #configuring canvas
        #canvas.get_tk_widget().configure(yscrollcommand=scroll_bar.set)
        #canvas.get_tk_widget().bind('<Configure>', lambda e: canvas.get_tk_widget().configure(scrollreigion=canvas.get_tk_widget().bbox("all")))

    def get_file(self):
        file_path = filedialog.askopenfilename()
        if not file_path:
            return
        self.audio_handler = AudioHandler(file_path)
        #exported_path = self.audio_handler.export()
        exported_path = self.audio_handler.export_sound_as_wav()
        file_name = exported_path.split('/')[-1]

        # Update file label & length
        self._file_frame.config(text=f"File: {file_name}")
        duration = self.audio_handler._sound.duration_seconds
        self._file_length.config(text=f"File Length: {duration:.2f}s")

        #self.get_resonance_freq()
        if self.spid_model is None:
            from Sound_Model import Spid_Model
            self.spid_model = Spid_Model(self)
            #updates resonance frequency label
            dom_freq = self.spid_model.resonance_freq(exported_path)
            self._file_freq.config(text=f"Resonance Frequency: {dom_freq} Hz")

    def plot_waveform(self):
        if self.audio_handler and self.spid_model:
            self.spid_model.waveform(self.audio_handler.export_sound_as_wav())


#test, delete later
disp = Spid_Displayer()