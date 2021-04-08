from  tkinter import *
root= Tk ()

root.geometry("500x400")
root.minsize(200,100)
root.maxsize(800,700)

label =Label(text = " Are You Ready ... ",bg= "black", fg= "white", padx=20, pady=20, borderwidth=8, relief= GROOVE)
label.pack(side=BOTTOM, padx=25,pady=25, fill=X)

root.mainloop()