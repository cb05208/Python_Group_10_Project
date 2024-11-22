# Base UI
from tkinter import *
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Set up main window
_root = Tk()
_root.title("Interactive Data Acoustic Modeling")
_root.geometry("650x700")
_root.config(pady=10)

# Choose file button
s = ttk.Style(_root)
s.configure('TButton',font=('Arial',12))
_file_btn = ttk.Button(
    _root, text="Pick File",style="TButton",padding="10 10 10 10")
_file_btn.grid(row=0,column=0,padx=25,pady=10,
                sticky='w')

# File label
_file_frame = ttk.Label(
    _root, text="filename.wav",
    font=10)
_file_frame.grid(row=0, column=1, sticky='w')

# Analyze file button
_analyze_btn = ttk.Button(
    _root, text="Analyze File",style="TButton",padding="10 10 10 10")
_analyze_btn.grid(row=0,column=2,pady=10,padx=155, sticky='e')

# Initial plot
f = Figure(figsize=(6,4), dpi=100)
plot1 = f.add_subplot(111)
plot1.plot()
plot1.set_title('Default Graph')
canvas = FigureCanvasTkAgg(f, _root)
canvas.draw()
canvas.get_tk_widget().grid(row=1,column=0,columnspan=4,pady=20,
                            sticky='w', padx=25)

# File length label
_file_length = ttk.Label(
    _root,text="File Length: 0s",font=('Arial',12),borderwidth=5,
    padding= '10 10 10 10',relief="groove")
_file_length.grid(row=2,column=0,padx=25,pady=10,sticky='w')

# Resonance freq label
_file_freq = ttk.Label(
    _root,text="Resonance Frequency: ___ Hz",font=('Arial',12),
    borderwidth=5, padding= '10 10 10 10',relief="groove")
_file_freq.grid(row=3,column=0,padx=25,pady=10,sticky='w',
                columnspan=2)

# RT60 difference label
_file_rtDiff = ttk.Label(
    _root, text="RT60 Difference: _._s",font=('Arial',12),
    borderwidth=5, padding= '10 10 10 10',relief="groove")
_file_rtDiff.grid(row=4,column=0,padx=25,pady=10)

# Waveform plot button
_waveform_btn = ttk.Button(
    _root, text="Waveform",style="TButton",padding="8 8 8 8")
_waveform_btn.grid(row=2,column=2,pady=10,sticky="w")

# Special plot button
special_btn = ttk.Button(
    _root, text="Special",style="TButton",padding="8 8 8 8")
special_btn.grid(row=3,column=2,pady=10,sticky="w")

# RT plot dropdown
options = [" Low", " Medium", " High"]
rt_in = StringVar()
rt_in.set("RT Plots")
rt_combobox = ttk.Combobox(_root, state="readonly", values=options,
                width=11,font=('Arial',12))
rt_combobox.set("     RT Plots")
rt_combobox.grid(row=2,column=2,pady=10,ipady=7)

# Combine plots button
combPlots_btn = ttk.Button(
    _root, text="Combine Plots",style="TButton",padding="8 8 8 8")
combPlots_btn.grid(row=3,column=2,pady=10)

_root.mainloop()