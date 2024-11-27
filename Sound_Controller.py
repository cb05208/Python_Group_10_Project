from Sound_Displayer import Spid_Displayer as sDisplay
from Sound_Model import Spid_Model as sModel
import tkinter as ttk
#IGNORE FOR NOW

'''
Purpose of the controller:
- create model and view
- 
'''

class Controller(ttk.Tk):
    #setting the model and view
    def __init__(self, sound_model, sound_display):
        super.__init__()
        self.sound_model = sound_model
        self.sound_display = sound_display

        view = sDisplay(self)
        view.grid(row=0, column=0, padx=10, pady=10)


if __name__ == '__main__':
    ctr = Controller()
    ctr.mainloop()