from tkinter import *

root = Tk ()
#GUI logic here
root.geometry('400x400')  # (widthxhieght)
root.minsize(200,250)     # (width, hieght)
#@root.maxsize(750,600)     # (width, hieght)
label = Label (text = "Welcome to learning of GUI in Pycharm")

label.pack()

root.mainloop()