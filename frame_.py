from tkinter import *

root = Tk ()
#GUI logic here
root.geometry('740x350')  # (widthxhieght)
root.minsize(200,250)     # (width, hieght)
root.maxsize(1500,900)     # (width, hieght)
root.title ("Jai Shree Ram")

f1 = Frame (root, bg ="sky blue", borderwidth = 6, relief=SUNKEN)         # frame makes blocks in our GUI window
f1.pack(anchor = "ne", side= TOP, fill=X)
akya= Label (f1, text = "File options ", font="comicsansms 13 italic", bg="pink", fg="red", pady= 20)
akya.pack()

f2 = Frame (root, bg= "black", borderwidth=5, relief = RIDGE)
f2.pack (side="left", fill=Y)
sethji= Label (f2, text= "Project Window",font="elephant 12 bold", bg="lime", fg="red")
sethji.pack(pady=140)


root.mainloop()