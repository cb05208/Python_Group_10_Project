#run this file
from Sound_Displayer import Spid_Displayer as sDisplay
from Sound_Model import Spid_Model as sModel
from Sound_Controller import Spid_Controller as sController


if __name__ == '__main__':
    view = sDisplay()
    model = sModel(view)    #eventually won't pass in displayer
    ctr = sController(model, view)
    view.mainloop()