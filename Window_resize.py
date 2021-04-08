from tkinter import *

def geom():
    wd=w_val.get()
    ht=h_val.get()
    root.geometry(f"{wd}x{ht}")

root =Tk()
root.geometry("500x500")

Label (text= "enter the dimensions you want ", font ="Arial 14 italic", padx=20, pady=10, relief=RAISED, borderwidth=7).grid(row=0, column=1, pady=11)
W = Label(root, text="Width -> ", font ="Arial 16 bold")
H = Label(root, text="Height -> ", font ="Arial 16 bold")

W.grid (row= 1, column=0, padx=10, pady=10)
H.grid (row= 2, column=0, padx=10, pady=10)

w_val = StringVar()
h_val = StringVar()

w_valentry = Entry (root, textvariable = w_val)
h_valentry = Entry (root, textvariable = h_val)

w_valentry.grid (row=1, column=1)
h_valentry.grid (row=2, column=1)

Button(text = "Submit", font ="comicsansms 16", padx=10, pady=10, command= geom).grid()

root.mainloop()