'''
Purpose of the controller:
- create model and view
- gets info from displayer object
- passes into model for analysis
- passes data from model into displayer to display the results
'''

class Spid_Controller():
    #setting the model and view, tk.Tk
    def __init__(self, sound_model, sound_display):
        #super().__init__()
        self.sound_model = sound_model
        self.sound_display = sound_display

        #view = sDisplay(self)
        #view.grid(row=0, column=0, padx=10, pady=10)