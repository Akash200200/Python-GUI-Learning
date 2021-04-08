from tkinter import *

root = Tk ()
#GUI logic here
root.geometry('420x540')  # (widthxhieght)
root.title ("Jai Shree Ram")

#frame = Frame (root, borderwidth=5, bg="pink", relief =SUNKEN)
frame = Frame (root, borderwidth=5, bg="pink", relief =SUNKEN)
frame.pack(side=TOP, anchor="nw")

b1 = Button(frame, fg="red", text= "print 1", padx=5, pady=5, borderwidth = 5, relief= RAISED)
b1.pack(side=LEFT, anchor = "ne")
b2 = Button(frame, fg="red", text= "print 2", padx=5, pady=5, borderwidth = 5, relief= RAISED)
b2.pack(side=LEFT, anchor = "se")
b3 = Button(frame, fg="red", text= "print 3", padx=5, pady=5, borderwidth = 5, relief= RAISED)
b3.pack(side= BOTTOM, anchor = "sw")
b4 = Button(frame, fg="red", text= "print 4", padx=5, pady=5, borderwidth = 5, relief= RAISED)
b4.pack(side=TOP, anchor = "nw")

root.mainloop()