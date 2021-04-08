from tkinter import *
import tkinter.messagebox as tmsg

r=Tk()
r.geometry("430x430")
r.title("Slider Learning")
def submit():
    a = tmsg.askyesno("Are you serious ?","Do you really Love her that much?")
    print(a)
    if a == 1:
        b = tmsg.showinfo("Msg from GOD", "Hang in there, She is your Lobster :)")


Label(text = "How much do you LOVE your Crush :)", font = " camicsansms 15 italic", borderwidth=5, relief = SUNKEN, pady=5, padx=15).pack(padx=15, pady=8, side=TOP, anchor ="nw")
loveslider = Scale (r,from_=0, to=10, orient=HORIZONTAL , tickinterval=1)
loveslider.pack()

Button(text="Yes Really",font = " Arial 14 italic", borderwidth=3, relief =RAISED, pady=5, padx=10, command=submit).pack()

photo = PhotoImage(file="heart.png")
akash = Label(image=photo)
akash.pack(side=BOTTOM)

r.mainloop()