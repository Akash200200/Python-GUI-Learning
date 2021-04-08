from tkinter import *

def getvalues():
    print (f"Username : {user_val.get()}")
    print (f"Password : {pasw_val.get()}")

root = Tk ()
#GUI logic here
root.geometry('540x350')  # (widthxhieght)
root.minsize(200,250)     # (width, hieght)
root.maxsize(1500,600)     # (width, hieght)
root.title ("Akash's GUI")

user = Label (root, text = "Username : ", font= "comicsansms 12 bold", borderwidth=6, relief = RAISED, padx= 10, pady=10)
pasw = Label (root, text = "Password : ", font= "comicsansms 12 bold", borderwidth=6, relief = RAISED, padx= 10, pady=10)

user.grid(row=0, column=0)
pasw.grid(row=1, column=0)

# types of variables in tkinter
# 1. BooleanVar 2.DoubleVar 3.IntVar 4.StringVar

user_val = StringVar()
pasw_val = StringVar()

userentry = Entry (root, textvariable = user_val)
paswentry = Entry (root, textvariable = pasw_val)

userentry.grid( row=0, column=1, padx=10, pady=10)
paswentry.grid(row = 1, column=1)

Button (text = "Submit", font= "comicsansms 12 bold", padx=10, pady=10, command= getvalues).grid()

root.mainloop()