from tkinter import *
#from PIL import Image, ImageTk   # to display image in .jpg format

root = Tk ()
#GUI logic here
root.geometry('700x500')  # (widthxhieght)
root.minsize(200,250)     # (width, hieght)
root.maxsize(850,600)     # (width, hieght)
label = Label (text = "Hello Akash, Welcome to learning of GUI in Pycharm")
label.pack()
pic = Label (text = "We found a childhood photo of you to start of with :) ")
pic.pack()

#displaying image in .jpg format
#image = Image.open ("akash_bheem.JPG")
#photo = ImageTk.PhotoImage(image)
#label = Label (image=photo)
#label.pack()                              # code not running for .jpg process

#displaying image in .png format
photo = PhotoImage(file="akash_bheem.png")
akash = Label (image = photo)
akash.pack()
#akash = Label (image = PhotoImage(file="akash_bheem.png"))

root.mainloop()