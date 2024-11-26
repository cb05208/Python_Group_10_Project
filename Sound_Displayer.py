# Base UI by Jessica Barker, View part of MVC
from tkinter import *
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import filedialog
import os
import numpy as np

class Spid_Displayer(tk.Tk):
    def __init__(self):
        #initializing window
        super().__init__()
        self.title("Interactive Data Acoustic Modeling")
        self.geometry("650x700")
        self.config(pady=10)
        self.minsize(650, 700)  #cannot make window smaller than 650x700

        self.create_buttons()
        
        self.mainloop()

    def create_buttons(self):
        #buttons!!!
        s = ttk.Style(self)
        s.configure('TButton', font=('Arial', 12))
        self._file_btn = ttk.Button(
            self, text="Pick File", style="TButton", command=self.get_file, padding="10 10 10 10")
        self._file_btn.grid(row=0, column=0, padx=25, pady=10,
                            sticky='w')

        # File label
        self._file_frame = ttk.Label(
            self, text="File name: ",
            font=10)
        self._file_frame.grid(row=0, column=1, sticky='w')

        # Analyze file button
        self._analyze_btn = ttk.Button(
            self, text="Analyze File", style="TButton", padding="10 10 10 10")
        self._analyze_btn.grid(row=0, column=2, pady=10, padx=155, sticky='e')

        # Initial plot
        f = Figure(figsize=(6, 4), dpi=100)
        plot1 = f.add_subplot(111)
        xvalues = np.arange(0, 12, 0.1)     #test values
        yvalues = np.sin(xvalues)   #test values
        plot1.plot(xvalues, yvalues, color='blue')
        plot1.set_title('Default Graph')
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0, columnspan=4, pady=20,
                                    sticky='w', padx=25)

        # File length label
        self._file_length = ttk.Label(
            self, text="File Length: 0s", font=('Arial', 12), borderwidth=5,
            padding='10 10 10 10', relief="groove")
        self._file_length.grid(row=2, column=0, padx=25, pady=10, sticky='w')

        # Resonance freq label
        self._file_freq = ttk.Label(
            self, text="Resonance Frequency: ___ Hz", font=('Arial', 12),
            borderwidth=5, padding='10 10 10 10', relief="groove")
        self._file_freq.grid(row=3, column=0, padx=25, pady=10, sticky='w',
                             columnspan=2)

        # RT60 difference label
        self._file_rtDiff = ttk.Label(
            self, text="RT60 Difference: _._s", font=('Arial', 12),
            borderwidth=5, padding='10 10 10 10', relief="groove")
        self._file_rtDiff.grid(row=4, column=0, padx=25, pady=10)

        # Waveform plot button
        self._waveform_btn = ttk.Button(
            self, text="Waveform", style="TButton", padding="8 8 8 8")
        self._waveform_btn.grid(row=2, column=2, pady=10, sticky="w")

        # Special plot button
        self.special_btn = ttk.Button(
            self, text="Special", style="TButton", padding="8 8 8 8")
        self.special_btn.grid(row=3, column=2, pady=10, sticky="w")

        # RT plot dropdown
        options = [" Low", " Medium", " High"]
        rt_in = StringVar()
        rt_in.set("RT Plots")
        rt_combobox = ttk.Combobox(self, state="readonly", values=options,
                                   width=11, font=('Arial', 12))
        rt_combobox.set("     RT Plots")
        rt_combobox.grid(row=2, column=2, pady=10, ipady=7)

        # Combine plots button
        self.combPlots_btn = ttk.Button(
            self, text="Combine Plots", style="TButton", padding="8 8 8 8")
        self.combPlots_btn.grid(row=3, column=2, pady=10)

    def get_file(self):
        file_path = filedialog.askopenfilename()
        file_name = os.path.basename(file_path)
        # print(file_name)
        if file_path:
            self._file_frame.config(text=f"File: {file_name}")  #setting message to display file name

#temporary test
disp = Spid_Displayer()