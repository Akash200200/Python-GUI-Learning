from tkinter import *

can_wd =500
can_ht = 400

root=Tk()

root.geometry(f"{can_wd}x{can_ht}")  # (widthxhieght)
root.minsize(200,250)     # (width, hieght)
root.maxsize(1700,1500)     # (width, hieght)
root.title ("Akash's GUI")

can_widget = Canvas (root, width= can_wd, height = can_ht)
can_widget.pack(fill=X)
can_widget.create_rectangle(0,0,1700,1500, fill="grey")        # working

root.mainloop()